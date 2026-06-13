# Calibration Prompts

Use these prompts to test whether the skill is producing ARTifacts rather than decorated explanations. A good result should lead with a bounded visual object, create wonder, preserve truth, and leave the human with clearer perception.

## First-Run Prompts

```text
/ensoul
```

Expected (the default register, and the headline promise): with no arguments, the skill ensouls whatever is already in view — the transcript, diff, decision, or conversation — and returns ONE small, glanceable artifact: a state card, bug trail, or before/after of a few lines. It must NOT produce a temple, mirror, or multi-panel plate for a bare invocation. A large or wild artifact from `/ensoul` alone is a failure (see "smallest shape that does the job" in SKILL.md). This is the one prompt that exercises what the README sells as the whole interface.

```text
Use $ensoul to show why generic AI dashboards feel dead. Give me an artifact, not an essay. Dense means picture-like, not more words.
```

Expected: a contained visual map showing how specificity, stakes, causality, or human context gets stripped into generic metrics.

```text
Use $ensoul to make a grounded symbolic mirror for someone who needs to make money soon without betraying taste, care, or deeper vows.
```

Expected: `recognition-pending`, a living network or symbolic field, one concrete next move, and an evidence drawer.

```text
Use $ensoul to explain coordination debt in a software team as an editorial plate inspired by Works in Progress. Spacious inside one visual frame.
```

Expected: topic-specific visual world, ornament-as-information, bounded negative space, and a mechanism visible at a glance.

```text
Use $ensoul in wild permission mode. Make something strange, jazz-like, ASCII-forward, and possibly wrong about why polished strategy decks kill live ideas.
```

Expected: a risky but coherent object with rhythm, asymmetry, and one real claim. Weirdness should reveal a structure, not replace one.

```text
Use $ensoul to compress this coding transcript into one visual state artifact: we changed a skill, tested Claude, found the border grammar was too wordy, tuned it toward wordless patterns, and now need to show what changed and what remains.
```

Expected: a Patch Room, Ready Field, or Review Altar using coding primitives. The artifact should show changed files/behavior, failures that shaped the patch, verification level, and remaining state.

```text
Use $ensoul to rewrite the opening of a README for this skill. A stranger should understand what the project does in the first screen.
```

Expected: a concrete before/after transformation or worked example first, not a taxonomy of artifact types or a visual map of Ensoul's internal grammar. The reader should see raw input become a useful artifact before encountering lineage, primitives, or philosophy.

## Failure Modes

| Failure | Smell | Repair |
| --- | --- | --- |
| Visual-ish essay | paragraphs with arrows sprinkled in | start over with the picture only |
| ASCII theater | impressive shapes with no claim | assign every mark a role |
| Generic sacredness | mystical language without evidence | add concrete forces, costs, and stakes |
| Scroll-drama | huge vertical whitespace | put air inside a 25-45 line frame |
| Corporate neatness | looks like a normal consulting slide | add one strange exact object |
| Data-viz cosplay | chart rules but no living insight | return to the public nerve |
| Flattery mirror | tells the human they are special | show both nutrient and rot |
| Coding postcard | pretty frame but no work state | add files/tests/failures/remaining state |
| Taxonomy portal | opens by mapping the skill instead of transforming material | lead with before/after |
| Completion inflation | says done when only partially verified | name the actual verification surface |

## Self-Evaluation

Score 0-2 for each:

| Gate | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Wonder | inert | mildly interesting | arresting |
| Recognition | generic | partly specific | "yes, that is the pattern" |
| Presence | automated | attentive | awake |
| Beauty | decorated | composed | form intensifies meaning |
| Truth | vague | plausible | grounded and inspectable |
| Goodness | manipulative or evasive | neutral | clarifies action with care |

If total is under 9, revise before shipping. If truth is under 1, do not ship.
