# CG — Continuous Generation Framework

CG provides **continuous documentation evolution** for AMPEL360.
It maintains cross-document coherence and grows technical documents gradually.

## Capabilities

| Mode | Function |
|---|---|
| `scan.py` | Detect missing links and plain ATA references |
| `generate.py` | Create missing documents + convert references to hyperlinks |
| `expand.py` | Expand underdeveloped sections with controlled depth |
| `score_relevance.py` | Ranks related documents (context inference, no embeddings) |

## Usage

### 1) Generate a Diagnostic Report (no changes made)
```bash
python tools/cg/scan.py
```

Output → `cd/reports/cg_scan_report.md`

### 2) Generate Missing Documents & Convert References
```bash
python tools/cg/generate.py
```

- Uses templates by default
- Enables contextual AI generation if `OPENAI_API_KEY` is set

### 3) Controlled Section Expansion
```bash
CG_MODE=BALANCED python tools/cg/expand.py
```

#### Available Growth Modes

| Mode | Behavior |
|---|---|
| `STEADY` | Minimal clarifications only |
| `BALANCED` (default) | Expand rationally and cleanly |
| `DEEPENING` | Add detailed technical reasoning |
| `EXPANSIVE` | Broader architectural/system integration context |

#### Safety Limits

| Variable | Default | Meaning |
|---|---|---|
| `CG_MAX_EDITS` | 25 | Max edits per run |
| `CG_SECTION_MIN_WORDS` | 120 | Threshold for expanding a section |

## Notes

- Only edits `.md` under `OPT-IN_FRAMEWORK/` and root documentation files.
- Never executes PR code; reads only.
- All changes are deterministic + reviewable.
