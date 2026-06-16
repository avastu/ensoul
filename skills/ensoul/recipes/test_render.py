#!/usr/bin/env python3
"""Unit tests for render.py — the deterministic core of ensoul.

Every generator is checked here so the growing recipe surface stays validatable:
alignment holds, ambiguous glyphs are flagged, data maps to ink faithfully, and
the beauty primitives are well-formed and deterministic. Run directly:

    python3 test_render.py        # prints "render tests ok (N checks)" or fails
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R

N = 0
def check(cond, msg):
    global N; N += 1
    assert cond, f"FAILED: {msg}"

# --- cells(): render-cell width, not code points ---------------------------
check(R.cells("abc") == 3, "ascii is one cell each")
check(R.char_cells("✓") == 1, "✓ is Neutral → 1 cell")
check(R.char_cells("·") == 1, "· ambiguous defaults to 1")
check(R.char_cells("·", ambiguous=2) == 2, "· renders 2 where ambiguous=wide")
check(R.char_cells("世") == 2, "CJK wide → 2 cells")
check(R.cells("é") == 1, "combining mark adds 0 width")

# --- audit(): flags the glyphs that drift a border -------------------------
check("·" in R.audit("a · b"), "· is flagged ambiguous")
check(R.audit("✓ ✕ plain ascii !?") == [], "neutral + ascii are clean")
check(R.audit("··") == ["·"], "audit de-dupes")

# --- spark_block: data → ink faithfully ------------------------------------
check(len(R.spark_block([1, 2, 3, 4])) == 4, "one cell per point")
idx = [R._BLOCKS.index(c) for c in R.spark_block([0, 1, 2, 3, 4])]
check(idx == sorted(idx), "increasing data → non-decreasing bars")
check(all(c in R._BLOCKS for c in R.spark_block([3, 1, 4, 1, 5])), "only block glyphs")

# --- hbar: proportional, exact width ---------------------------------------
check(len(R.hbar(0.5, 20)) == 20, "hbar respects width")
check(R.hbar(0.0, 10) == "░" * 10, "frac 0 → all track")
check(R.hbar(1.0, 10) == "█" * 10, "frac 1 → all fill")
check(R.hbar(0.5, 10).count("█") == 5, "frac 0.5 → half fill")

# --- open_frame: forgiving form, cannot drift ------------------------------
of = R.open_frame("T", [" ✓ a", " ◎ b longer line"])
check("│" not in of and "┐" not in of, "open frame has no right border")
rule = of.splitlines()[1]
check(R.cells(rule) >= max(R.cells(l) for l in of.splitlines()[2:]), "rule spans content")

# --- measured_box: holds, and warns honestly -------------------------------
box, warns = R.measured_box("CLEAN", ["  all ascii content  "])
widths = {R.cells(l) for l in box.splitlines()}
check(len(widths) == 1, "every box line is equal render-width")
check(warns == [], "clean content → no warnings")
_, w2 = R.measured_box("OK", ["has a · dot"])
check(w2 and "·" in w2[0], "ambiguous content is warned")
_, w3 = R.measured_box("title ·", ["clean"])
check(w3 and "·" in w3[0], "ambiguous title is warned too")

# --- terrain: a real series as a faithful landscape ------------------------
t = R.terrain([0, 1, 2, 3, 4], width=10, height=5).splitlines()
check(len(t) == 5, "terrain row count == height")
check(t[-1][0] != " ", "lowest value still fills the floor")
check(t[0].rstrip() != "" and t[0][0] == " ", "peak fills the top only on the high side")
check(R.terrain([1, 5, 2]) == R.terrain([1, 5, 2]), "terrain is deterministic")

# --- wave / orb: well-formed and deterministic -----------------------------
wv = R.wave(width=30, height=7).splitlines()
check(len(wv) == 7, "wave row count == height")
check(all(c in R._SHADE for row in wv for c in row), "wave uses only shade glyphs")
check(R.wave() == R.wave(), "wave is deterministic")
check("█" in R.orb(radius=6), "orb has a bright core")
check(R.orb() == R.orb(), "orb is deterministic")

# --- field: scalar function → ink ------------------------------------------
full = R.field(lambda nx, ny: 1.0, width=8, height=3).splitlines()
check(full == ["█" * 8] * 3, "field of 1.0 is solid")
empty = R.field(lambda nx, ny: 0.0, width=8, height=3).splitlines()
check(all(r == "" for r in empty), "field of 0.0 is blank")

# --- golden recipe: exponential backoff spiral -----------------------------
spiral = R.exponential_backoff_spiral()
check("EXPONENTIAL BACKOFF" in spiral, "spiral has a clear title")
check(all(str(i) in spiral for i in range(1, 5)), "spiral labels attempts 1-4")
check("wait 1s" in spiral and "wait 2s" in spiral and "wait 4s" in spiral, "spiral names widening waits")
check("success or give up" in spiral, "spiral names the exit condition")
check("gaps widen" in spiral, "spiral states the mechanism")
check(R.exponential_backoff_spiral() == spiral, "spiral is deterministic")

# --- surface attunement: fold detail away from the edge ---------------------
known = R.surface_width(dial="balanced", surface_cols=100)
check(known == 92, "known surface width keeps breathing room")
unknown = R.surface_width(dial="balanced")
check(unknown == 68, "unknown balanced surface uses a conservative default")
wide = R.flow_row("├─ hot history", "Timeseries store ──▶ dashboards", "0-30d", width=96)
check(len(wide.splitlines()) == 1 and "[0-30d]" in wide, "wide known surfaces may keep the qualifier inline")
folded = R.flow_row("├─ hot history", "Timeseries store ──▶ dashboards", "0-30d", width=56)
folded_lines = folded.splitlines()
check(len(folded_lines) == 2, "narrow/unknown surfaces fold secondary detail downward")
check("[0-30d]" not in folded_lines[0], "primary path stays clear of the edge")
check("0-30d" in folded_lines[1], "folded qualifier is preserved")
check(max(R.cells(line) for line in folded_lines) <= 56, "folded output fits the target width")
unknown_folded = R.flow_row("├─ hot history", "Timeseries store ──▶ dashboards", "0-30d")
check(len(unknown_folded.splitlines()) == 2, "unknown surfaces fold qualifiers near the wrap cliff")

print(f"render tests ok ({N} checks)")
