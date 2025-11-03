from fastapi import FastAPI, Request, Header, HTTPException, Depends
from fastapi.responses import JSONResponse
import hmac, hashlib, os, sqlite3, json
from typing import Optional
from pathlib import Path

DB_PATH = Path("./data/prs.db")
GITHUB_SECRET = os.getenv("GITHUB_SECRET", "")
MCP_TOKEN = os.getenv("MCP_TOKEN", "change-me")

app = FastAPI(title="MCP PR-memory (AMPEL)")

# DB helpers
def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS prs (
        number INTEGER PRIMARY KEY,
        title TEXT,
        summary TEXT,
        state TEXT,
        closed_at TEXT,
        url TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# Basic auth dependency for MCP clients
async def require_token(authorization: Optional[str] = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    if not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization scheme")
    token = authorization.split(" ", 1)[1]
    if token != MCP_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return True

# GitHub signature verification
def verify_signature(body: bytes, signature_header: str) -> bool:
    if not GITHUB_SECRET:
        return False
    mac = hmac.new(GITHUB_SECRET.encode(), body, hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature_header)

@app.post("/webhook")
async def webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None)):
    body = await request.body()
    if not x_hub_signature_256 or not verify_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Invalid signature")
    payload = await request.json()
    # handle pull_request closed/merged
    action = payload.get("action")
    if action == "closed" and "pull_request" in payload:
        pr = payload["pull_request"]
        number = pr["number"]
        title = pr.get("title", "")
        merged = pr.get("merged", False)
        state = "merged" if merged else "closed"
        closed_at = pr.get("closed_at")
        summary = (pr.get("body") or "")[:2000]
        url = pr.get("html_url")
        conn = sqlite3.connect(DB_PATH)
        conn.execute("INSERT OR REPLACE INTO prs (number, title, summary, state, closed_at, url) VALUES (?, ?, ?, ?, ?, ?)",
                     (number, title, summary, state, closed_at, url))
        conn.commit()
        conn.close()
    # optionally handle push events (index recent commits) - omitted for brevity
    return JSONResponse({"ok": True})

@app.get("/search_prs")
async def search_prs(q: str = "", limit: int = 10, _: bool = Depends(require_token)):
    def escape_like(s: str) -> str:
        # Escape backslash first, then % and _
        return s.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    escaped_q = escape_like(q)
    like = f"%{escaped_q}%"
    cur.execute(
        "SELECT number, title, summary, state, closed_at, url FROM prs WHERE title LIKE ? ESCAPE '\\' OR summary LIKE ? ESCAPE '\\' ORDER BY closed_at DESC LIMIT ?",
        (like, like, limit)
    )
    rows = cur.fetchall()
    conn.close()
    results = []
    for r in rows:
        results.append({
            "id": f"pr-{r[0]}",
            "type": "pull_request",
            "name": f"PR #{r[0]} - {r[1]}",
            "uri": r[5],
            "content": {"summary": r[2], "state": r[3], "closed_at": r[4]}
        })
    return {"resources": results}

@app.get("/get_diff")
async def get_diff(pr: int, _: bool = Depends(require_token)):
    # Placeholder: in a more complete implementation fetch diff from GitHub via API or stored diffs
    return {"pr": pr, "diff": "(diff not stored; implement GitHub API fetch here)"}

@app.get("/manifest")
async def manifest(_: bool = Depends(require_token)):
    # Minimal MCP manifest
    m = {
        "version": "2025-01-01",
        "id": "ampl-pr-memory",
        "name": "AMPEL PR Memory MCP",
        "resources_endpoint": "/search_prs",
        "tools": [
            {"name": "search_prs", "description": "Buscar PRs cerrados/mergeados", "endpoint": "/search_prs"},
            {"name": "get_diff", "description": "Obtener diff bajo demanda", "endpoint": "/get_diff"}
        ]
    }
    return m
