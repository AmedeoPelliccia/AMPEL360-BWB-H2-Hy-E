#!/usr/bin/env python3
"""
PUB BREX Guard (SVG/XML)

Purpose:
- Whenever SVG/XML files under /PUB/ are modified, enforce:
  1) CSDB root contains BREX artifacts
  2) DM XML includes BREX reference (brexDmRef or equivalent)
  3) Naming patterns for DMC/PMC/DML/ICN are sane/deterministic
  4) XML/SVG are well-formed
  5) DM dmCode / issueInfo / language align with filename tokens (best-effort)

This is designed to make Copilot "do the right thing" by failing PRs that
do not honor BREX and CSDB rules.

Usage:
  python tools/ci/pub_brex_guard.py

Env:
  BASE_SHA, HEAD_SHA: git SHAs used for diff
  MODEL_ID: expected modelIdentCode (default AMPEL360AT)
"""

from __future__ import annotations

import os
import re
import sys
import subprocess
from dataclasses import dataclass
from pathlib import Path
import xml.etree.ElementTree as ET


RE_XML = re.compile(r".*\.(xml|XML)$")
RE_SVG = re.compile(r".*\.(svg|SVG)$")


# Allow both ICN forms:
#  - ICN-AMPEL360AT-23-10-0001-A_001.SVG
#  - ICN-AMPEL360AT-23-10-00-0001-A_001.SVG
def icn_ok(name: str, model_id: str) -> bool:
    n = name.upper()
    mid = model_id.upper()
    pat_a = rf"^ICN-{re.escape(mid)}-\d{{2}}-\d{{2}}-\d{{4}}-[A-Z]_\d{{3}}\.SVG$"
    pat_b = rf"^ICN-{re.escape(mid)}-\d{{2}}-\d{{2}}-\d{{2}}-\d{{4}}-[A-Z]_\d{{3}}\.SVG$"
    return re.match(pat_a, n) is not None or re.match(pat_b, n) is not None


# DMC canonical (as you are using):
# DMC-{MODEL}-{SYSDIFF}-{SYS}-{SEC}-{SBJ}-{ASSY}{DIS}{DISVAR}-{INFO}{INFOVAR}-{ILC}_{ISSUE}-{INWORK}_{LANG}-{COUNTRY}.XML
RE_DMC = re.compile(
    r"^DMC-(?P<model>[A-Za-z0-9]+)-(?P<sysdiff>[A-Za-z0-9]+)-(?P<sys>\d{2})-(?P<sec>\d{2})-(?P<sbj>\d{2})-"
    r"(?P<assy>\d{2})(?P<dis>\d{2})(?P<disvar>[A-Za-z0-9])-(?P<info>\d{3})(?P<infovar>[A-Za-z0-9])-(?P<ilc>[A-Za-z0-9])_"
    r"(?P<issue>\d{3})-(?P<inwork>\d{2})_(?P<lang>[A-Za-z]{2})-(?P<country>[A-Za-z]{2})\.XML$",
    re.IGNORECASE,
)

# PMC is project-defined in your repo; keep it permissive but deterministic
RE_PMC = re.compile(
    r"^PMC-(?P<model>[A-Za-z0-9]+)-(?P<issuer>[A-Za-z0-9]+)-(?P<number>[A-Za-z0-9\-]+)_(?P<issue>\d{3})-(?P<inwork>\d{2})_(?P<lang>[A-Za-z]{2})-(?P<country>[A-Za-z]{2})\.XML$",
    re.IGNORECASE,
)

RE_DML = re.compile(
    r"^DML-(?P<model>[A-Za-z0-9]+)-(?P<listid>[A-Za-z0-9\-]+)_(?P<issue>\d{3})-(?P<inwork>\d{2})_(?P<lang>[A-Za-z]{2})-(?P<country>[A-Za-z]{2})\.XML$",
    re.IGNORECASE,
)

BREX_HINT_KEYS = ("brex", "BREX", "brexDm", "brex_dm", "brexDmRef", "brexRef")


@dataclass
class Finding:
    level: str  # "ERROR" or "WARN"
    path: str
    message: str


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def git_diff_files(base: str, head: str) -> list[str]:
    # --diff-filter=AM to catch added/modified; renames also show as changes in name list.
    out = run(["git", "diff", "--name-only", "--diff-filter=AMR", base, head])
    return [x for x in out.splitlines() if x.strip()]


def is_pub_artifact(p: str) -> bool:
    return "/PUB/" in p.replace("\\", "/") and (RE_XML.match(p) or RE_SVG.match(p))


def find_csdb_root(path: Path) -> Path | None:
    # Identify the directory ending with ".../CSDB"
    parts = path.parts
    for i in range(len(parts), 0, -1):
        if parts[i - 1].upper() == "CSDB":
            return Path(*parts[:i])
    return None


def parse_xml(path: Path) -> ET.ElementTree | None:
    try:
        return ET.parse(path)
    except (ET.ParseError, FileNotFoundError, PermissionError, OSError):
        return None


def tag_endswith(elem: ET.Element, suffix: str) -> bool:
    # handle namespaces: "{ns}dmodule"
    return elem.tag.lower().endswith(suffix.lower())


def first_kb_text(path: Path, max_bytes: int = 4096) -> str:
    try:
        with path.open("rb") as f:
            return f.read(max_bytes).decode("utf-8", errors="replace")
    except Exception:
        return ""


def ensure_brex_present(csdb_root: Path) -> tuple[bool, str]:
    brex_dir = csdb_root / "BREX"
    if not brex_dir.exists() or not brex_dir.is_dir():
        return False, f"Missing BREX directory at: {brex_dir}"
    # Require at least one XML in BREX/
    brex_xml = list(brex_dir.glob("*.xml")) + list(brex_dir.glob("*.XML"))
    if not brex_xml:
        return False, f"BREX directory exists but contains no XML: {brex_dir}"
    return True, ""


def ensure_csdb_profile_mentions_brex(csdb_root: Path) -> tuple[bool, str]:
    # Accept either:
    #   .../PUB/AMM/csdb.profile.yaml
    # or .../PUB/AMM/CSDB/csdb.profile.yaml
    # or .../PUB/AMM/CSDB/profile.yaml (rare)
    candidates = [
        csdb_root / "csdb.profile.yaml",
        csdb_root / "CSDB.profile.yaml",
        csdb_root / "profile.yaml",
        csdb_root.parent / "csdb.profile.yaml",
    ]
    prof = next((p for p in candidates if p.exists()), None)
    if not prof:
        return False, f"Missing csdb.profile.yaml (searched: {', '.join(str(c) for c in candidates)})"
    # Limit read size to prevent memory exhaustion with large files
    max_profile_size = 64 * 1024  # 64 KB should be plenty for profile files
    if prof.stat().st_size > max_profile_size:
        return False, f"{prof} is unexpectedly large (>{max_profile_size} bytes)."
    txt = prof.read_text(encoding="utf-8", errors="replace")
    if not any(k in txt for k in BREX_HINT_KEYS):
        return False, f"{prof} does not appear to mention BREX (expected a brex/brexDmRef/brex_dm key)."
    return True, ""


def validate_dm_filename_vs_dmcode(path: Path, tree: ET.ElementTree, model_id: str) -> list[Finding]:
    findings: list[Finding] = []
    m = RE_DMC.match(path.name)
    if not m:
        findings.append(Finding("ERROR", str(path), "Filename is not a valid DMC pattern for this repo."))
        return findings

    root = tree.getroot()
    if not tag_endswith(root, "dmodule"):
        findings.append(Finding("ERROR", str(path), "Expected DM root element <dmodule> (namespace allowed)."))
        return findings

    dmcode = root.find(".//dmCode")
    if dmcode is None:
        findings.append(Finding("ERROR", str(path), "Missing <dmCode> in DM ident section."))
        return findings

    # dmCode attributes
    def a(k: str) -> str:
        return (dmcode.attrib.get(k) or "").strip()

    expected_model = model_id
    if a("modelIdentCode") and a("modelIdentCode") != expected_model:
        findings.append(Finding("ERROR", str(path), f"dmCode modelIdentCode='{a('modelIdentCode')}' != '{expected_model}'."))

    # Best-effort filename alignment check (only if attributes are present)
    # Compare SYS/SEC/SBJ
    for attr, grp, label in [
        ("systemDiffCode", "sysdiff", "systemDiffCode"),
        ("systemCode", "sys", "systemCode"),
        ("subSystemCode", "sec", "subSystemCode"),
        ("subSubSystemCode", "sbj", "subSubSystemCode"),
        ("assyCode", "assy", "assyCode"),
        ("disassyCode", "dis", "disassyCode"),
        ("disassyCodeVariant", "disvar", "disassyCodeVariant"),
        ("infoCode", "info", "infoCode"),
        ("infoCodeVariant", "infovar", "infoCodeVariant"),
        ("itemLocationCode", "ilc", "itemLocationCode"),
    ]:
        v = a(attr)
        if v and v.upper() != m.group(grp).upper():
            findings.append(
                Finding("ERROR", str(path), f"Filename token {grp}='{m.group(grp)}' != dmCode {label}='{v}'.")
            )

    # Issue / Language alignment (best-effort)
    issue = root.find(".//issueInfo")
    if issue is not None:
        inum = issue.attrib.get("issueNumber", "").strip()
        iwrk = issue.attrib.get("inWork", "").strip()
        if inum and inum != m.group("issue"):
            findings.append(Finding("ERROR", str(path), f"Filename issue='{m.group('issue')}' != issueInfo.issueNumber='{inum}'."))
        if iwrk and iwrk != m.group("inwork"):
            findings.append(Finding("ERROR", str(path), f"Filename inWork='{m.group('inwork')}' != issueInfo.inWork='{iwrk}'."))
    lang = root.find(".//language")
    if lang is not None:
        lc = lang.attrib.get("languageIsoCode", "").strip()
        cc = lang.attrib.get("countryIsoCode", "").strip()
        if lc and lc.upper() != m.group("lang").upper():
            findings.append(Finding("ERROR", str(path), f"Filename lang='{m.group('lang')}' != languageIsoCode='{lc}'."))
        if cc and cc.upper() != m.group("country").upper():
            findings.append(Finding("ERROR", str(path), f"Filename country='{m.group('country')}' != countryIsoCode='{cc}'."))
    return findings


def dm_has_brex_ref(tree: ET.ElementTree) -> bool:
    root = tree.getroot()
    # Accept any of these as "BREX is being checked/used"
    # You can tighten this later to ONLY accept brexDmRef.
    # First check element tags for brex (efficient)
    for e in root.iter():
        if "brex" in e.tag.lower():
            return True
        # Also check element text and attribute values
        if e.text and "brex" in e.text.lower():
            return True
        for attr_val in e.attrib.values():
            if "brex" in str(attr_val).lower():
                return True
    return False


def validate_svg(path: Path, model_id: str) -> list[Finding]:
    findings: list[Finding] = []

    if not icn_ok(path.name, model_id):
        findings.append(Finding("ERROR", str(path), "ICN filename does not match allowed ICN patterns for this repo."))

    # SVG must be well-formed XML
    tree = parse_xml(path)
    if tree is None:
        findings.append(Finding("ERROR", str(path), "SVG is not well-formed XML."))
        return findings

    root = tree.getroot()
    if not tag_endswith(root, "svg"):
        findings.append(Finding("ERROR", str(path), "Root element is not <svg> (namespace allowed)."))

    if "viewBox" not in root.attrib:
        findings.append(Finding("ERROR", str(path), "SVG missing viewBox attribute (required for publication scaling)."))

    # Disallow external raster/image refs (publication hygiene)
    # Flag any <image> node or xlink:href/href with http(s)
    for e in root.iter():
        if e.tag.lower().endswith("image"):
            findings.append(Finding("WARN", str(path), "SVG contains <image> element. Prefer pure vector for AMM/IPC."))
        href = e.attrib.get("href") or e.attrib.get("{http://www.w3.org/1999/xlink}href")
        if href and (href.startswith("http://") or href.startswith("https://")):
            findings.append(Finding("ERROR", str(path), f"SVG contains external reference href='{href}'. Not allowed."))

    # Require header comment with filename + model id (forces traceability in generated artifacts)
    head = first_kb_text(path, 4096)
    if path.name not in head:
        findings.append(Finding("ERROR", str(path), "SVG header must include the exact filename (for traceability)."))
    if model_id not in head:
        findings.append(Finding("ERROR", str(path), f"SVG header must mention MODEL_ID '{model_id}'."))
    return findings


def validate_pub_file(path: Path, model_id: str) -> list[Finding]:
    findings: list[Finding] = []
    csdb = find_csdb_root(path)
    if csdb is None:
        findings.append(Finding("ERROR", str(path), "File is under /PUB/ but no CSDB root was found in its path."))
        return findings

    ok, msg = ensure_brex_present(csdb)
    if not ok:
        findings.append(Finding("ERROR", str(path), msg))

    ok, msg = ensure_csdb_profile_mentions_brex(csdb)
    if not ok:
        findings.append(Finding("ERROR", str(path), msg))

    # Validate by type
    if RE_XML.match(path.name):
        # CSDB XML: DM / PM / DML etc
        tree = parse_xml(path)
        if tree is None:
            findings.append(Finding("ERROR", str(path), "XML is not well-formed."))
            return findings

        upper_name = path.name.upper()
        if upper_name.startswith("DMC-"):
            # enforce DMC pattern and dmCode alignment
            findings.extend(validate_dm_filename_vs_dmcode(path, tree, model_id))

            # enforce BREX reference (hard gate)
            if not dm_has_brex_ref(tree):
                findings.append(
                    Finding(
                        "ERROR",
                        str(path),
                        "DM must include a BREX reference (e.g., <brexDmRef> in dmStatus).",
                    )
                )
        elif upper_name.startswith("PMC-"):
            if not RE_PMC.match(path.name):
                findings.append(Finding("ERROR", str(path), "PMC filename does not match repo PMC pattern."))
        elif upper_name.startswith("DML-"):
            if not RE_DML.match(path.name):
                findings.append(Finding("ERROR", str(path), "DML filename does not match repo DML pattern."))
        else:
            # Other XML types: still require model token if it is a CSDB artifact
            if "AMPEL360" in upper_name and model_id.upper() not in upper_name:
                findings.append(Finding("WARN", str(path), f"XML filename includes AMPEL360 but not MODEL_ID '{model_id}'. Verify naming."))
    else:
        # SVG
        findings.extend(validate_svg(path, model_id))

    return findings


def main() -> int:
    base = os.getenv("BASE_SHA", "").strip()
    head = os.getenv("HEAD_SHA", "").strip()
    model_id = os.getenv("MODEL_ID", "AMPEL360AT").strip()

    if not base or not head:
        print("ERROR: BASE_SHA and HEAD_SHA must be set by the workflow.", file=sys.stderr)
        return 2

    try:
        changed = git_diff_files(base, head)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: git diff failed: {e}", file=sys.stderr)
        return 2

    pub_targets = [f for f in changed if is_pub_artifact(f)]
    if not pub_targets:
        print("No /PUB/ SVG/XML changes detected. Nothing to check.")
        return 0

    findings: list[Finding] = []
    for f in pub_targets:
        p = Path(f)
        if not p.exists():
            # file could be renamed; ignore missing paths here
            continue
        findings.extend(validate_pub_file(p, model_id))

    # Summarize
    errors = [x for x in findings if x.level == "ERROR"]
    warns = [x for x in findings if x.level == "WARN"]

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        sp = Path(summary_path)
        # Validate that GITHUB_STEP_SUMMARY path is under expected runner directories
        try:
            resolved = sp.resolve()
            # GitHub Actions step summary is typically under /home/runner or /github
            valid_prefixes = ("/home/runner", "/github", "/tmp")
            if not any(str(resolved).startswith(prefix) for prefix in valid_prefixes):
                print(f"WARNING: GITHUB_STEP_SUMMARY path '{resolved}' is outside expected directories", file=sys.stderr)
                summary_path = None
        except (OSError, ValueError):
            summary_path = None
    if summary_path:
        sp = Path(summary_path)
        with sp.open("a", encoding="utf-8") as s:
            s.write("## PUB BREX Guard Results\n\n")
            s.write(f"- Files checked: **{len(pub_targets)}**\n")
            s.write(f"- Errors: **{len(errors)}**\n")
            s.write(f"- Warnings: **{len(warns)}**\n\n")
            if errors:
                s.write("### Errors (must fix)\n")
                for e in errors:
                    s.write(f"- `{e.path}` — {e.message}\n")
                s.write("\n")
            if warns:
                s.write("### Warnings\n")
                for w in warns:
                    s.write(f"- `{w.path}` — {w.message}\n")
                s.write("\n")

    # Console output (annotations-friendly)
    for f in findings:
        print(f"{f.level}: {f.path}: {f.message}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
