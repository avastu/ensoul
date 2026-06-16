#!/usr/bin/env python3
"""Deterministic quality bar for an ensoul end-to-end run.

`scripts/validate` proves the recipes are correct in isolation. This proves the
*lived install* still works: a cold agent that reads only the skill installs it,
configures by SHOWING (not asking), records + honors global defaults, and emits
drift-free artifacts in the right form. It reads the captured outputs of one
`scripts/e2e` run and asserts behavioural properties — not exact bytes, because
agent output is non-deterministic. The human resonance panel judges feel; this
judges that the floor held.

Usage:  e2e_assert.py <out-dir> <config-dir> <skill-dir>
  out-dir     captured turn logs: t1.txt t2.txt t3.txt wall1..6.txt validate.txt
  config-dir  the jailed CLAUDE_CONFIG_DIR (expects skills/ensoul + CLAUDE.md)
  skill-dir   the installed skill (for recipes/render.py: cells/audit)
"""
import os
import re
import sys

SPARK = "▁▂▃▄▅▆▇█"

results = []  # (ok: bool, critical: bool, label, detail)


def check(ok, label, detail="", critical=True):
    results.append((bool(ok), critical, label, detail))


def read(path):
    try:
        return open(path, encoding="utf-8").read()
    except OSError:
        return ""


def fenced_blocks(text):
    """Return the contents of each ``` fenced block."""
    return re.findall(r"```[^\n]*\n(.*?)```", text, re.DOTALL)


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    out, config, skill = sys.argv[1], sys.argv[2], sys.argv[3]
    sys.path.insert(0, os.path.join(skill, "recipes"))
    try:
        from render import cells, audit
    except Exception as e:  # pragma: no cover
        print(f"could not import render.py from {skill}/recipes: {e}")
        return 2

    # --- A · install landed -------------------------------------------------
    skill_md = os.path.join(config, "skills", "ensoul", "SKILL.md")
    check(os.path.isfile(skill_md), "install", f"skill at {skill_md}")

    # --- B · self-validation passed ----------------------------------------
    v = read(os.path.join(out, "validate.txt"))
    check("validation ok" in v, "validate", "ran clean on the installed copy")
    m = re.search(r"render tests ok \((\d+) checks\)", v)
    check(m and int(m.group(1)) >= 33, "render-tests",
          f"{m.group(1) if m else '?'} checks")

    # --- C · configure BY SHOWING (the hardened behaviour) ------------------
    t1 = read(os.path.join(out, "t1.txt"))
    blocks1 = fenced_blocks(t1)
    check(len(blocks1) >= 3, "configure-by-showing",
          f"{len(blocks1)} rendered blocks in the configure turn (need >=3: plain/balanced/wild)")

    # --- D · defaults recorded globally ------------------------------------
    cmd = read(os.path.join(config, "CLAUDE.md"))
    check(bool(cmd), "global-memory-file", "CLAUDE.md written")
    check(re.search(r"dial", cmd, re.I) and
          re.search(r"plain|balanced|wild", cmd, re.I), "dial-recorded")
    check(re.search(r"mode", cmd, re.I) and
          re.search(r"on.?demand|standing", cmd, re.I), "mode-recorded")

    # --- E · defaults HOLD in a fresh session ------------------------------
    t3 = read(os.path.join(out, "t3.txt"))
    reask = re.search(r"which dial|plain.{0,3}balanced.{0,3}or.{0,3}wild|"
                      r"on.?demand or standing", t3, re.I)
    check(bool(fenced_blocks(t3)) and not reask, "defaults-persist",
          "cold session produced an artifact without re-asking config")

    # --- F · each wall produced the right kind of artifact -----------------
    EXPECT = {  # wall -> (min_block_lines, must-contain predicate or None, why)
        1: (4, None, "trail"),
        2: (4, None, "card"),
        3: (4, None, "flow"),
        4: (3, lambda b: any(c in b for c in SPARK), "sparkline for the series"),
        5: (12, None, "wild image, not timid"),
        6: (12, None, "wild image, not timid"),
    }
    for n, (minlines, pred, why) in EXPECT.items():
        path = os.path.join(out, f"wall{n}.txt")
        if not os.path.exists(path):
            continue  # not run (e.g. --configure-only) — don't judge an absent wall
        blks = fenced_blocks(read(path))
        big = max((b for b in blks), key=len, default="")
        ok = bool(blks) and len(big.strip().splitlines()) >= minlines
        if pred:
            ok = ok and pred(big)
        check(ok, f"wall{n}-form", why)

    # --- G · no closed-box DRIFT anywhere (Bowie's core complaint) ----------
    # A *true* closed box is the only form that can drift: a top corner row
    # `┌…┐`, body rows `│…│`, a bottom `└…┘`. Open frames, left-spines, and
    # flow diagrams (lone `│` connectors, `└──▶` branches) have no right edge
    # to drift, so they are correctly ignored here.
    #   FAIL  rows differ in render-width under ambiguous=1  -> visibly broken
    #   warn  equal at 1 but differ at ambiguous=2           -> cross-font risk
    def closed_boxes(blk):
        lines, i, boxes = blk.splitlines(), 0, []
        while i < len(lines):
            s = lines[i].strip()
            if s.startswith("┌") and s.endswith("┐"):
                box, j = [lines[i]], i + 1
                while j < len(lines):
                    t = lines[j].strip()
                    if t.startswith("│") and t.endswith("│"):
                        box.append(lines[j]); j += 1
                    elif t.startswith("└") and t.endswith("┘"):
                        box.append(lines[j]); boxes.append(box); i = j; break
                    else:
                        break
            i += 1
        return boxes

    drift, fragile = [], []
    for src in ["t1", "t2", "t3", "wall1", "wall2", "wall3", "wall4", "wall5", "wall6"]:
        for blk in fenced_blocks(read(os.path.join(out, f"{src}.txt"))):
            for box in closed_boxes(blk):
                rows = [r.rstrip("\n") for r in box]
                if len({cells(r, 1) for r in rows}) > 1:
                    drift.append(f"{src}: closed box rows differ at 1-cell width "
                                 f"{sorted({cells(r,1) for r in rows})}")
                elif len({cells(r, 2) for r in rows}) > 1:
                    fragile.append(f"{src}: closed box holds at 1-cell but drifts under "
                                   f"ambiguous=2 (font-dependent glyph inside)")
    check(not drift, "no-box-drift", "; ".join(drift) or "closed boxes hold equal width",
          critical=True)
    check(not fragile, "box-robust-cross-font",
          "; ".join(fragile) or "closed boxes robust under ambiguous-width fonts",
          critical=False)

    # --- report -------------------------------------------------------------
    width = max(len(l) for _, _, l, _ in results)
    crit_fail = 0
    warn_fail = 0
    print("\n  ENSOUL E2E QUALITY BAR\n  " + "-" * 58)
    for ok, critical, label, detail in results:
        mark = "PASS" if ok else ("FAIL" if critical else "warn")
        if not ok:
            crit_fail += critical
            warn_fail += (not critical)
        print(f"  [{mark}]  {label.ljust(width)}  {detail}")
    print("  " + "-" * 58)
    if crit_fail:
        print(f"  {crit_fail} critical check(s) failed — the floor moved. do not ship.")
        return 1
    if warn_fail:
        print(f"  passed with {warn_fail} warning(s) — review before shipping.")
    else:
        print("  e2e quality bar: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
