#!/usr/bin/env python3
"""Token-cost ledger for the ensoul skill — part of the ship process.

Run before shipping any change to the skill's prose, references, or recipes:

    python3 recipes/token_cost.py

It reports cost by LOAD TIER, because "total size" is the wrong number — what
matters is what loads, and when. Estimates are ~chars/4 (a portable heuristic,
labeled ≈; Claude's tokenizer differs, but the tiers and deltas are what guide
decisions). The point is to keep the HOT path (always-on + on-trigger + the
files pulled on most runs) lean, and let cold references be as rich as they earn.
"""
from __future__ import annotations
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rp(*p): return os.path.join(ROOT, *p)
def chars(path): return len(open(path, encoding="utf-8").read())
def tok(c): return round(c / 4)

# --- tier classification -----------------------------------------------------
# Hot = loads on most real runs. Cold = pulled rarely, one at a time.
HOT_REFS = set()   # post-migration: examples live in forms/ (load one); gallery = install meta, recipe-api = optional
SOURCE   = {"render.py"}                                 # read ONLY to change a recipe (cheatsheet calls it)
DEVONLY  = {"test_render.py", "token_cost.py"}           # never enter model context

def skill_split():
    """(always_on_desc_chars, on_trigger_body_chars) for SKILL.md."""
    t = open(rp("SKILL.md"), encoding="utf-8").read()
    m = re.search(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    if not m:
        return 0, len(t)
    front, body = m.group(1), m.group(2)
    d = re.search(r"description:\s*\|?\s*\n?(.*)", front, re.S)
    desc = d.group(1) if d else front
    return len(desc), len(body)

def main():
    desc_c, body_c = skill_split()
    rows = []  # (tier, label, chars)
    rows.append(("always-on", "SKILL.md · description (discovery)", desc_c))
    rows.append(("on-trigger", "SKILL.md · body", body_c))
    for f in sorted(glob.glob(rp("forms", "*.md"))):
        rows.append(("form-lazy", f"forms/{os.path.basename(f)}", chars(f)))
    for f in sorted(glob.glob(rp("references", "*.md"))):
        name = os.path.basename(f)
        tier = "hot-lazy" if name in HOT_REFS else "cold-lazy"
        rows.append((tier, f"references/{name}", chars(f)))
    for f in sorted(glob.glob(rp("recipes", "*.py"))):
        name = os.path.basename(f)
        if name in DEVONLY:
            tier = "dev-only"
        elif name in SOURCE:
            tier = "source"
        else:
            tier = "source"
        rows.append((tier, f"recipes/{name}", chars(f)))

    order = ["always-on", "on-trigger", "form-lazy", "hot-lazy", "cold-lazy", "source", "dev-only"]
    print(f"\n  ensoul · token cost by load tier        (≈ chars/4)\n  {'='*58}")
    by_tier = {}
    for tier in order:
        group = [r for r in rows if r[0] == tier]
        if not group:
            continue
        sub = sum(c for _, _, c in group)
        by_tier[tier] = sub
        print(f"  {tier}")
        for _, label, c in sorted(group, key=lambda r: -r[2]):
            print(f"      {label:44} {tok(c):>5} tok")
        if len(group) > 1:
            print(f"      {'— subtotal —':44} {tok(sub):>5} tok")
    print(f"  {'-'*58}")

    # --- what a real run costs: ONE form, not the library --------------------
    always  = by_tier.get("always-on", 0)
    trig    = by_tier.get("on-trigger", 0)
    forms   = [c for t, _, c in rows if t == "form-lazy"]
    avg_f   = round(sum(forms) / len(forms)) if forms else 0
    max_f   = max(forms) if forms else 0
    gallery = next((c for t, l, c in rows if l.endswith("materials-gallery.md")), 0)
    install = trig + sum(forms) + gallery
    print(f"  always-on (every turn, ensoul or not)        {tok(always):>5} tok")
    print(f"  runtime /ensoul  (body + ONE form)           {tok(trig + avg_f):>5} tok"
          f"   · heaviest form → {tok(trig + max_f)}")
    print(f"  install / first run  (body + all forms + shelf) {tok(install):>5} tok")
    print(f"  {'='*58}")
    print(f"  runtime loads 1 of {len(forms)} forms (avg {tok(avg_f)} tok), never the library.")
    print(f"  keep always-on + on-trigger lean; richness lives in forms/ + cold refs.\n")

if __name__ == "__main__":
    main()
