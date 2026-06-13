---
name: ensoul
description: |
  Use when complex context, coding work, bug hunts, project state, architecture, strategy, research, reviews, or emotionally loaded material needs a visual artifact instead of a normal summary. Also use when designing or critiquing diagrams, maps, dashboards, reports, visual essays, glyph systems, ASCII/Unicode artifacts, symbolic mirrors, patterned frames, or public-facing explanations. Every artifact balances three loads: truth (it does not lie), beauty (form and meaning intensify each other), and goodness (it leaves the person clearer and more sovereign, never manipulated).
---

# Ensoul

Create visual artifacts for felt understanding.

The lived purpose: when an agent produces more text than a person can take in — and their eyes start to slide off the wall — Ensoul returns one small shape they can read at a glance. It is reader-protection against the wall, not decoration.

Ensoul turns complex work into bounded artifacts where line, silence, symbol, pattern, and evidence let truth become felt before it is fully explained. Use it for research communication, project state, coding transcripts, strategy, architecture, agent behavior, symbolic mirrors, public explainers, ASCII/Unicode artifacts, and visual essays.

## The Three Loads

Every Ensoul artifact carries three loads at once. They are equal weight. An artifact that aces one and fails another does not ship.

```text
  TRUTH     it does not lie. visual weight matches real
            evidence, and proof sits next to its claim.

  BEAUTY    form and meaning intensify each other. nothing
            is decoration; nothing earns its place by being
            pretty alone.

  GOODNESS  it leaves the person clearer and more sovereign —
            never manipulated, flattered, exposed, or rushed
            by how good the picture looks.
```

Truth keeps it honest. Beauty makes it land. Goodness keeps it *for the person* instead of a performance aimed at them. When the three conflict, do not resolve it by force — usually the move is to subtract until all three can hold at once.

The three gates below are how you check each load. The modes and workflow are how you make the artifact in the first place.

## Default Register

Default to the **smallest artifact that does the job**: one move, a few lines, glanceable in a single look. This restrained end of the range is the default — Rubin before cathedral. A reader should grasp it without decoding a legend or parsing more than one relationship at a time.

A bare `/ensoul` invocation takes whatever is in front of it — the transcript, the diff, the decision, the conversation — and returns one small, honest, glanceable shape at this register. The user should not have to specify anything; bare `/ensoul` is the whole interface.

The user can set a standing **dial** — `plain`, `balanced`, or `wild` — usually chosen once at install and recorded **globally** in the agent's own memory/instructions, so it holds across all of their projects. It shifts the default along one axis: how much plain text versus visual wildness/abstraction they want. `plain` leans on words with a few marks; `balanced` is the small glanceable visual described here (and the default when the dial is unset); `wild` makes the default a **striking single-image artifact** — commit to one dominant visual metaphor (a sun, a constellation, a tide, a creature) and render the content *into* it. On `wild`, enter Wild Permission Mode below and **do not fall back to a tidy card, list, or timeline** — that is the failure. If the result looks like something `balanced` would produce, it is not wild enough; push further. (The README's radiant-sun "day" is the target register.) Honor the dial when it is set; a per-invocation request ("go wild," "just words") overrides it for that turn. Whatever the dial, the no-lie / no-dazzle gates still hold and bare invocations stay bounded.

The user also chooses a **mode**, again usually at install. In **on-demand** mode they invoke Ensoul explicitly (`/ensoul`, or `$ensoul` in Codex). In **standing** (automatic) mode the agent applies Ensoul to its own output going forward: whenever a reply would land as a wall of text, lead with the artifact instead of the wall. Standing mode still respects the dial, keeps artifacts bounded, and still returns a plain sentence when a sentence is clearest — it does not decorate short replies.

**Configure from the user's own material, not abstract description.** At install (or first run), take a real recent artifact from their environment — a transcript, a diff, the project's state, a file they just touched — and render it at all three dial settings: `plain`, `balanced`, `wild`. Let them pick the dial by seeing Ensoul on their own work, then capture the dial and the mode and record both **globally** in the agent's memory/instructions, so they hold across the user's projects. Showing it on their material is the demo and the configuration in one move; never make them choose `plain`/`balanced`/`wild` from words alone.

Reach for larger, denser, or stranger forms — mirrors, editorial plates, 25–45-line wild compositions — **only when the user asks** (in the moment, or via a standing `wild` dial) for "more," "bigger," "wild," "a plate," "a mirror." Absent that, a bare invocation stays small even when the input is huge: compress to the few things that matter (aim for ~3–7 lines). If the material truly has too many live threads to hold in one glance, surface the top few and ask what to focus on — do **not** silently expand into a dense map. Range is available on request; restraint is the default. If you find yourself making a big artifact for a bare invocation, stop and ship the small one.

And if a plain sentence is already the clearest form, return the sentence — not a box around it. A glyph frame on "the meeting is at 3pm" is theater; "3pm" is the honest answer. The no-artifact reply is a legitimate Ensoul output, not a failure to perform.

## Core Lineage

The lineage maps onto the three loads:

- **Tufte** — *truth:* evidence, integrity, comparison, graphical honesty under the beauty.
- **Ruth Asawa** — *beauty:* line, loop, shadow, delicacy, spacious structure.
- **Rick Rubin** — *beauty by subtraction:* essence, presence, the one true thing.
- **Works in Progress / Stripe Press** — *beauty as cognition:* ornament that is information.
- **Psychomagic** — *goodness:* symbols grounded in real forces, costs, and choices, used to free perception, not to cast a spell.

Keep the public surface grounded. The deeper charge belongs in the artifact, not in vague mystical claims.

## Concrete Transformation Gate

Default to **show the transformation**, not the taxonomy.

Before making a mythic map, temple, mirror, or editorial plate, identify the smallest concrete input and the useful output it should become. If the audience is new to the project, lead with a before/after artifact unless another form is clearly more useful.

```text
BEFORE
"We fixed the login bug, tests pass locally, prod deploy is still pending."

AFTER ENSOUL
┌──────────── LOGIN FLOW ────────────┐
│ ◎ behavior  session persists        │
│ ✕ old path  logged users out        │
│ Δ patch     retry refresh once      │
│ ✓ proof     regression test passed  │
│ ~ open      prod deploy pending     │
└─────────────────────────────────────┘
```

Use the abstract visual system only after the concrete transformation is visible. A stranger should be able to answer, within a few seconds: "What did this skill do to the input?"

If the first artifact explains Ensoul, the project, or the visual grammar more than it transforms the user's material, revise toward a before/after, state card, bug map, or concrete worked example. (Performing the skill instead of serving the person is a goodness failure — see the Goodness Gate.)

## Show-Not-Tell Preference

When the topic is complex, prefer a compact visual before long prose. When the user asks for creativity, make the artifact feel alive, but make every flourish encode meaning.

- Use a diagram or concept map for structure.
- Use a causal or process flow for mechanism.
- Use a timeline for sequence.
- Use a comparison table or small multiples for alternatives, tradeoffs, or variants.
- Use an annotated artifact sketch when a concrete example can carry the explanation.
- Use a glyph legend, ASCII/Unicode map, atlas page, or semiotic key when the subject has recurring forces, organs, gates, risks, or states.
- Use an image-like editorial plate when the response should be felt and remembered, not merely summarized.
- Use visual primitives deliberately: center, threshold, plinth, aperture, spire, band, lattice, procession, orbit, root, scar, gate, vessel, and field.
- Treat borders and frames as semantic surfaces. A rich frame can encode evidence, pressure, lineage, constraints, rhythm, weather, or provenance; it should not be a decorative box.
- For coding collaboration, use intuitive coding primitives: `✓` verified proof, `▤` file/receipt, `✕` failure/risk, `!` urgency, `Δ` change, `◆` design/decision, `?` unknown, `~` unstable, `▲` user-visible feature, `◎` behavior at the center, `o──o` dependency/handoff.

Make the visual do real explanatory work. Add prose to interpret the visual, not to replace it.

## Output Contract

When producing an artifact:

1. Lead with the artifact itself, usually in a fenced `text`, `mermaid`, HTML/SVG, image prompt, table, or compact mixed-media layout.
2. For first-contact, README-like, onboarding, or explanatory outputs, prefer a concrete before/after transformation over a map of the skill's categories.
3. Make the artifact legible without the prose tail.
4. Keep interpretation short: one paragraph or 3 bullets unless the user asks for a deeper read.
5. Put evidence, assumptions, or caveats under the artifact as a small drawer, not as the main event.
6. Do not apologize for weirdness. Explain only the symbols that are not self-evident.

If the first draft feels like a paragraph with decorations, revise toward a picture: reduce sentences, increase spatial relationships, labels, contrast, and marks that mean something.

## Truth Gate

Beauty does not exempt the artifact from rigor. Before shipping, check that it does not lie:

1. **Story** — what comparison, mechanism, state, or decision is this meant to reveal? If there is no answer, the artifact is decoration.
2. **Integrity** — does visual weight match actual evidence and importance? Never make weak evidence look central, verified, or urgent.
3. **Comparison** — does the viewer know "compared to what?" Show the alternative, baseline, before/after, or counterfactual when comparison matters.
4. **Evidence** — are receipts, assumptions, scales, sources, tests, and verification levels close to the claims they support? Keep a compact evidence drawer beneath the artifact.
5. **Tufte spine** (for charts and quantitative displays) — lie factor ≈ 1.0, proportional scales, real baselines, no 3D distortion, minimal chartjunk, high data-ink ratio, clear labels, and appropriate small multiples. See `references/tufte-principles.md`.

For personal, strategic, identity, relationship, or values mirrors, label the artifact `recognition-pending` until the human explicitly says it lands. Elegance is not evidence.

## Beauty Gate

Beauty is not styling laid on top of an idea; it is form and meaning intensifying each other. Before shipping, check that the form earns itself:

1. **Eraser** — for every mark, word, border, glyph, label, tick, line, ornament, or annotation: can it be erased without losing information or felt structure? If yes, erase it.
2. **Collision** — mentally box every text label and dense mark cluster. Does another label, line, border, or symbol cross or crowd it? Move, lighten, separate, or remove.
3. **Layering** — does primary meaning dominate while secondary structure recedes? Borders and ornament should support the center, not fight it.
4. **Wonder** — is there a small intake of breath, surprise, or curiosity, or does it read like a tidy workplace diagram?
5. **Presence** — does it feel attended to, specific, and awake, rather than generated or generically ornamental?
6. **Intensification** — would the idea be weaker without this form? If the styling could be stripped and the meaning survive unchanged, the beauty is decoration. Make the beauty carry the mechanism.

To push beauty further when the user invites it, see Wild Permission Mode and the Works in Progress / Stripe Press inspiration below.

## Goodness Gate

Truth and beauty can both be present and the artifact can still harm: a gorgeous, accurate picture that quietly manipulates, flatters, exposes, or leaves the person dependent on its spell. Goodness is the load that keeps the artifact in service of the person's own seeing and freedom. Before shipping, check that it is *for them*:

1. **Non-manipulation** — beauty must never smuggle a conclusion past the evidence. If the composition makes the viewer *feel* that something is proven, urgent, or settled when the evidence does not support it, it is lying with style. Lower the visual weight to match the truth.
2. **Sovereignty** — does the artifact leave the person more able to see, decide, and act on their own, or more dependent on the maker's cleverness? Aim to hand back power, not to dazzle.
3. **No false weather** — do not manufacture urgency, certainty, doom, or hype through visual force. Let what is calm look calm; mark only what is genuinely at risk.
4. **Care under load** — for emotionally loaded, vulnerable, or cruelty-prone material (a person's failures, a relationship, someone's life), hold it without wounding or exposing. Reduce confusion and cruelty. A mirror should let someone meet themselves, not flinch from a verdict.
5. **Honest blind spots** — name what the artifact cannot see. A clean frame implies completeness; say what was excluded, assumed, or unknown so the tidiness is not itself a lie.
6. **Recognition over seduction** — for anything that mirrors a person's values, life, or direction, the goal is "yes, that is the pattern," not "wow." Hold `recognition-pending` until they say it lands; never self-certify that it landed.

Goodness is not softness. It can mean showing a hard truth plainly. It refuses two opposite failures: **cruelty** (wounding without care) and **flattery** (comfort that hides consequence).

## Wild Permission Mode

When the user explicitly asks for weirder, wilder, Rick-Rubin-like, Ruth-Asawa-like, jazz-like, appalling, wrong, risky, or permission-to-fail artifacts — **or whenever their dial is set to `wild`** — loosen the usual politeness and produce a stranger designed object. This mode is not optional decoration on `wild`; it is the job. Lead with one dominant unforgettable image and bend the content into it.

Use this mode to:
- privilege surprise, rhythm, silence, negative space, repetition, loops, knots, syncopation, and sculptural line;
- make ASCII/Unicode feel like wire, score, ritual diagram, net, stage direction, or found inscription;
- let the artifact risk being ugly, excessive, asymmetrical, haunted, funny, or wrong;
- create one dominant unforgettable image before explaining anything;
- keep a hidden skeleton of integrity: symbols still mean something, and the artifact still reveals a real structure.

Do not sand off the interesting edge just because the result may be confusing. In this mode, failure is allowed if the failure teaches taste. The three loads still apply: even a wild artifact must not lie (truth), must intensify rather than decorate (beauty), and must not manipulate or wound the person it is for (goodness).

Spaciousness means air inside a bounded visual window, not making the user scroll through emptiness. Prefer one contained frame with tension, silence, and negative space over a tall artifact that disperses attention.

Target shape:
- one visual window, usually 25-45 lines unless the user asks for a long scroll piece;
- clear outer boundary or compositional center;
- fewer labels, stronger marks;
- one strange focal object;
- enough air that the eye can move, not so much that the artifact becomes a pause button.

## Artifact-First Stance

"Dense" usually means perceptually dense, not word-dense. Prefer a single designed object over a long explanation when the object can carry the structure.

An artifact can be:
- a one-page concept plate;
- a mycelial network map;
- a glyph atlas;
- an evidence confection;
- a visual essay frame;
- a psychomagic mirror for values, attention, or inner conflict;
- a small-multiple field of worlds, options, or states;
- a diagram that feels like a painting because its composition is doing epistemic work.

Before writing paragraphs, ask: "What would the reader understand if they only saw the artifact?"

## Symbolic Mirror Mode

Use this mode when the ask touches strategy, identity, creative direction, agent behavior, relationships, memory, values, or "what is really going on?"

Design the artifact like a living network:
- **Hyphae:** subtle links, dependencies, traces, affordances, and latent paths.
- **Nodes:** people, ideas, commitments, organs, risks, memories, offers, proofs, and artifacts.
- **Nutrients:** attention, trust, money, evidence, energy, beauty, legitimacy, time.
- **Fruiting bodies:** visible outputs: pages, products, decisions, offers, essays, rituals, releases.
- **Rot:** stale beliefs, dead projects, debt, shame loops, hidden bottlenecks, uninspected costs.
- **Symbiosis:** mutual benefit, shared context, handoffs, alliances, honest reciprocity.

Psychomagic does not mean vague mysticism. It means the image changes what can be perceived and therefore what can be acted on. Keep it grounded: every symbol should correspond to a real force, evidence trace, decision, or lived tension.

Symbolic mirrors are where the Goodness Gate matters most. The material is loaded and the person is exposed in their own reflection. Do not claim the artifact is true because it is elegant. Include a compact evidence drawer with the observed prompt/context signals, hold the result as `recognition-pending`, and hold the person with care rather than verdict.

When the input is emotionally raw, or about another person's hidden intentions, do not arrange unverifiable psychology into a confident shape — a `recognition-pending` label does not redeem an artifact that still overclaims what cannot be known. Default instead to a plain **known / unknown / next question** frame: what the evidence actually shows, what it cannot, and the next thing to check. Earn the fuller mirror only when there is real signal to ground it.

## Works in Progress / Stripe Press Inspiration

Take visual inspiration from Works in Progress and Stripe Press without copying their house style. The useful principles are:

- **Ornament as cognition:** an image, texture, etching, glyph, or historical fragment can be information, not decoration.
- **Topic-specific worlds:** each idea deserves its own visual atmosphere so it can be remembered as itself.
- **Beauty invites difficulty:** a beautiful artifact can ask the reader to lean in, puzzle, and reread.
- **Historical freshness:** old diagrams, engravings, ledgers, type specimens, maps, and marginalia can feel new when recontextualized truthfully.
- **Easter eggs with purpose:** strange details are allowed when they encode the subject's mechanism or leak meaning across the composition.
- **Public progress lens:** make underrated ideas legible, vivid, and socially consequential.

When this influence matters, read `references/editorial-artifact-patterns.md`.

## Workflow

### For research communication and complex explanations:

1. **Find the public nerve**
   - What is the deep claim, mechanism, or surprise?
   - What does the audience currently misunderstand?
   - What emotional/intellectual tension should pull them through?

2. **Choose a visual grammar**
   - Structure or ontology -> concept map, network, matrix, or atlas.
   - Mechanism -> causal flow, state machine, sequence, or swimlane.
   - Research evidence -> annotated table, small multiples, evidence strip, or figure-plus-caption.
   - Strategy or tradeoff -> 2x2, frontier curve, decision table, or force-field map.
   - Living/systemic metaphor -> organism map, organs table, feedback loop, glyph legend.
   - Lived meaning or identity -> psychomagic mirror, mycelial field map, symbolic atlas, or ritual plate.
   - Public-explainer topic -> editorial plate, historical collage, annotated image, or visual essay frame.

3. **Assign meaning to marks**
   - Position, size, value, texture, color, orientation, shape, enclosure, and arrows should mean something.
   - Include a legend when symbols are non-obvious.
   - Let aesthetics intensify the encoding; do not let aesthetics replace it.

4. **Anchor the wonder**
   - Show evidence, provenance, assumptions, or uncertainty where relevant.
   - Preserve causality and mechanism.
   - If making a wild or poetic artifact, keep a visible spine: inputs -> transformation -> outputs -> consequences.

5. **Run the three gates**
   - **Truth:** weight matches evidence; "compared to what?" answered; receipts near claims; lie factor honest for any chart.
   - **Beauty:** eraser and collision passed; primary meaning dominates; form intensifies rather than decorates.
   - **Goodness:** no conclusion smuggled past the evidence; no false urgency; loaded material held with care; blind spots named.

6. **Ship a memorable artifact**
   - Prefer one dense visual/table/diagram that can be reread over paragraphs that merely describe.
   - Use words, numbers, images, and symbols together.
   - Make the reader feel the shape of the idea.
   - If the prompt asks for magic, make the beauty carry the mechanism.

### For new visualizations:

1. **Clarify the data story**
   - What comparisons matter?
   - What's the key insight to communicate?
   - Who's the audience?

2. **Select approach** using Tufte principles:
   - High comparison need → Small multiples
   - Dense data → Consider data tables, sparklines
   - Time-series → Line charts with minimal grid
   - Part-to-whole → Avoid pie charts; prefer bar/table

3. **Design with data-ink in mind**
   - Start minimal, add only what's necessary
   - Every element must earn its ink
   - Default to grayscale; use color purposefully

4. **Run the three gates** (Truth, Beauty, Goodness above), with extra attention to the Tufte spine: erase redundant elements, duplicate encodings, and heavy gridlines; check every text element's bounding box; move explanatory prose into captions when it crowds the plot; push reference labels to margins or connect them with leader lines.

5. **Apply the Tufte spine in detail** (see `references/tufte-principles.md`).

### For critiquing visualizations:

1. **Check graphical integrity** (truth) — calculate lie factor if proportions seem off, verify baselines and scales, look for 3D distortion.
2. **Identify chartjunk** (beauty) — decorative elements, heavy grids, unnecessary 3D effects, moiré patterns; ask what can be erased.
3. **Check whom it serves** (goodness) — does the display mislead, manufacture urgency, or flatter a desired conclusion? Does it hide what it cannot show?
4. **Suggest improvements** with specific before/after recommendations.

## Triad Checklist

Run before shipping any artifact:

- [ ] **TRUTH** — visual weight matches evidence; "compared to what?" is answered; proof sits near its claim; lie factor ≈ 1.0 for charts; meaning-bearing mirrors held `recognition-pending`.
- [ ] **BEAUTY** — every mark survives the eraser; no collisions; primary meaning dominates and ornament recedes; form intensifies the idea instead of decorating it; symbols carry meaning, not vibes.
- [ ] **GOODNESS** — no conclusion smuggled past the evidence; no false urgency or false certainty; loaded material held with care, not cruelty or flattery; blind spots named; the person is left more sovereign.
- [ ] When the three conflict, subtract until all three can hold at once.

## Key Principles Reference

- `references/tufte-principles.md` — core principles from *Visual Display of Quantitative Information*: lie factor, data-ink, chartjunk, small multiples, integrity. (Truth.)
- `references/analytical-design.md` — extensions from *Envisioning Information*, *Visual Explanations*, and *Beautiful Evidence*: the 6 principles of analytical design, sparklines, layering & separation, micro/macro, range-frames, causality, confections. Load when designing dashboards, dense displays, sparklines, or explanatory graphics.
- `references/visual-language-research-communication.md` — graphic-language and research-communication patterns inspired by semiology of graphics, diagrams, networks, maps, visual variables, evidence confections, and public technical storytelling. Load when explaining research, systems, strategy, architecture, agent behavior, or complex ideas to humans.
- `references/editorial-artifact-patterns.md` — WIP/Stripe Press-inspired editorial art direction, ornament-as-information, and grounded symbolic artifact patterns. Load when the user asks for magic, artifacts, mycelial networks, publication-quality visuals, or public-facing explainers. (Beauty.)
- `references/visual-primitives.md` — reusable mark grammar and compositional primitives inspired by temple architecture, editorial plates, ASCII art, living systems, and coding collaboration. Load when inventing a new artifact style, making a glyph system, tuning visual language, or summarizing coding/project state.
- `references/calibration-prompts.md` — first-run prompts, failure modes, and self-evaluation patterns. Load when testing, tuning, installing, or validating the skill.

## Cross-Agent Use

This skill is intentionally compatible with Codex and Claude Code skill formats: a folder with `SKILL.md` plus optional `references/` and `assets/`. To keep both agents aligned, update the source skill and mirror the whole folder into Claude's personal skills directory at `~/.claude/skills/ensoul/`. In Claude Code, the command name comes from the directory, so invoke it as `/ensoul`; in Codex the trigger is `$ensoul`.

This plain skill folder is the canonical source.
