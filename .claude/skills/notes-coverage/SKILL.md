---
name: notes-coverage
description: Audit a student's class notes, slides or worksheets so nothing on them is missed before teaching, quizzing or writing a summary for an exam. Use whenever the student shares study material (PDF, photos, screenshots of notes) for an upcoming test, asks "what do I need to know/memorize", asks for a question bank or cheat sheet from their file, or asks "was this in the file?". Catches small handwritten teacher notes, crossed-out worked examples, missing pages and hidden prerequisite formulas.
---

# Notes Coverage Audit

Goal: before teaching from a student's material, build a complete map of everything on it, then make sure every item is either taught or explicitly flagged to the student as skipped. The student should never walk into an exam and meet something that was in their file but never mentioned.

## Why this exists

On a Chemistry SBQ (Ch 16 buffers/titration notes), the teacher had hand-written a tiny "H⁺ M×V = M×V OH⁻" next to "Equivalence point" on p.13, and the worked titration calculations (n = M × V, [H⁺] = mmol ÷ total volume) were scribbled through. Both were treated as "not needed", molarity was never taught, and the exam asked for the weak acid's molar concentration at the equivalence point. Small marks and crossed-out pages still carry methods.

## Procedure

### 1. Inventory pages first
- Read the page numbers printed on each page (footer/header), not the PDF's own page count.
- List any gaps (e.g. "you sent pp. 1–5, 7–11, 13–15, 17–19, 25; missing 6, 12, 16, 20–24").
- Tell the student at the start and ask for the missing pages before building anything. If they can't, say plainly which topics might be on them.

### 2. Read every page at a resolution where handwriting is legible
- Default page renders are often too small for margin notes. For an annotation pass, render each page larger, e.g. `pdftoppm -r 150 -f N -l N -png file.pdf out`, and look at the full page.
- Look specifically between lines, in margins, above headings and next to arrows. Teachers squeeze formulas into those spaces.

### 3. Record every teacher signal, verbatim, with its location
Capture each of these as its own row:
- Handwritten words: "Define", "Calculate", "Label", "Graph", "Example", "How they work", "Know this".
- Handwritten formulas or symbols, however small (e.g. `M×V = M×V`, `ratio = 1`, `pKa ± 1`).
- Circled, boxed, starred, underlined or highlighted items.
- Printed boxes such as "IMPORTANT NOTE" or "IMPORTANT EXAM NOTE" — copy these word for word.
- "Questions: solve X–Y" lists that point to textbook problems.

### 4. Never drop crossed-out content silently
Crossed-out usually means "you won't have to do this full calculation", not "this method won't appear".
- For each crossed-out block, write down the underlying skills it uses (e.g. mmol = M × mL, divide by total volume, pH = −log[H⁺], excess reactant).
- Teach those skills briefly even if the full calculation is skipped.
- Tell the student it was crossed out and ask whether the teacher said it's excluded.

### 5. List hidden prerequisites
Write out the formulas and ideas the notes use without stating them, e.g. molarity (M = mol ÷ L), mmol = M × mL, concentration after mixing = mmol ÷ total mL, pH = −log[H⁺], pKa = −log Ka, Ka × Kb = Kw. Each becomes a row in the map.

### 6. Build the coverage map
Keep it as a table (in a file in the workspace when files are available, otherwise in chat):

| Page | Item (verbatim or short) | Type | Teacher signal | Taught | Quizzed |
|---|---|---|---|---|---|
| 13 | Equivalence point: M×V = M×V | handwritten formula | arrow + circle | ☐ | ☐ |
| 13–17 | Titration calcs (n = M×V, ÷ total V) | crossed out | scribbled | ☐ | ☐ |

Types: definition, concept, formula, worked example, graph/label, handwritten note, crossed-out method, exam note, prerequisite, missing page.

### 7. Teach and quiz from the map
- Order: items with a teacher signal first, then the rest.
- Every quiz question cites its page. Say when a question or its answer choices were written by you rather than taken from the file.
- Tick the Taught/Quizzed columns as you go.

### 8. Coverage check before any "you're ready"
Before saying all topics are covered, or producing a final summary, cheat sheet or "what to memorize" list:
- Walk the map. Every row must be taught, or flagged to the student with the reason (missing page, crossed out and confirmed excluded, out of time).
- Put every handwritten formula and every hidden prerequisite on the final sheet, even as one line.
- Tell the student in one short list what was not covered.

### 9. After the exam
Ask what came up that wasn't covered. Find where it was in the material and add the miss to "Why this exists" above as a new example, so the same kind of item is caught next time.
