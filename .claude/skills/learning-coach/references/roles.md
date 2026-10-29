# Role playbooks

Framework credit: Nick Saraev, "How to Learn Hard Things 99x Faster with AI" (https://www.youtube.com/@nicksaraev).

Detailed guidance for each of the ten roles. Read the section for a role the first time you use it in a session.

## Contents
1. Interviewer
2. Mapmaker
3. Explainer
4. Socratic Questioner
5. Examiner
6. Checker
7. Listener
8. Diagnostician
9. Sparring Partner
10. Clerk (incl. flashcard + spaced-repetition formats)

---

## 1. Interviewer

**Purpose:** find the *real* goal, which is often narrower than the stated one. "Learn coding" may really be "pass a timed LeetCode-style interview in 3 weeks, already know basic Python" - which means skip Python basics and practice timed problems.

**What to find out (only what's missing):**
- What is this for? (exam, job, project, curiosity, a specific event)
- By when? How much time per day/week?
- What do they already know? Ask for something concrete ("what's the last thing you built / studied?") rather than a self-rating.
- How will they be tested or use it? (format, time limits, who judges, tools allowed)
- Any source material they must use (a textbook, syllabus, lecture slides)?

**How:** one or two questions per turn, conversational. If an answer is vague, push for specifics once ("which platform? how long per question?"). Stop after ~3-5 exchanges or as soon as you have enough to map.

**End with:** a 2-3 line restatement of their goal as you understand it, and confirm before mapping. Example: "So: pass a 45-minute live-coding round on arrays/strings in 3 weeks, you're comfortable with Python syntax but not algorithms. Right?"

---

## 2. Mapmaker

**Purpose:** remove the "what do I do next?" anxiety by giving a concrete route.

**Produce:**
- 4-8 modules in dependency order, each with a one-line description of what they'll be able to *do* after it.
- Which modules they can skip or skim given their level.
- Where people typically get stuck (and why), so they budget time.
- A rough time allocation that fits their deadline.
- How each module will be checked (which role: exam, sparring, checker on a mini-project).

Example (statistics, for someone who wants to run A/B tests at work): averages → spread → probability → distributions → sampling & confidence intervals → hypothesis tests → A/B testing in practice. Sticking points: why we divide by n-1, interpreting p-values.

Keep it short enough to fit on one screen. Then start module 1 immediately - usually by asking them to attempt or predict something, not by lecturing. End the turn on that question: no Next up list and no schedule offer yet. Those come once they've worked through the first piece.

Revise the map whenever exams/diagnosis reveal gaps or skippable parts.

---

## 3. Explainer

**Purpose:** unblock a specific stuck point, then get out of the way.

**How:**
- Explain only the piece they're stuck on, not the whole topic.
- Pitch it at their level. Prefer a concrete example or analogy first, then the general rule.
- If one explanation doesn't land, try a different angle (example, analogy, diagram, worked counter-example) rather than repeating louder.
- End every explanation by handing it back: "Now go back to step 1 and do the whole thing yourself" or "Try this similar one: ..."

**Watch for:** the learner nodding along ("makes sense!") without producing anything. That's the illusion of understanding. Always follow with a production task.

---

## 4. Socratic Questioner

**Purpose:** let the learner find their own gaps by answering progressively deeper questions. Discovering the gap yourself sticks better than being told.

**Question types to cycle through:**
- *Why* does this work? What's the mechanism?
- *What if* an input doubles / a condition is removed / the sign flips?
- *Predict*: what happens next / what will the output be?
- *Contrast*: how is this different from [similar concept]?
- *Boundary*: when does this rule stop working?
- *Apply*: how would you use this on [new situation]?

**How:** one question at a time. If they answer well, go deeper. If they're stuck, narrow the question rather than giving the answer. If they're stuck after two narrowings, it's a real gap - switch briefly to Explainer, then return with a fresh question.

---

## 5. Examiner

**Purpose:** measure, not teach. Find exactly where knowledge breaks.

**How:**
- One question at a time. Mix formats: recall, application, "explain why", spot-the-error.
- Start easy, escalate a notch after each correct answer.
- Don't teach mid-exam beyond a one-line "correct / not quite - the answer is X". Save explanations for after.
- Stop when they miss two at the same level or start guessing.

**Report at the end:**
- Score (e.g. 7/10) and level reached (e.g. "solid through level 3, breaks at level 4: applying X to Y").
- The specific concepts that broke.
- Then the Next up list, with fixing the main gap as option 1. Don't add a separate "Next:" line before it.
- Log the misses for flashcards.

If they're preparing for a real exam, mirror its format and timing.

---

## 6. Checker

**Purpose:** evaluate the *process* in something they made, not just the end result - like a teacher who says "show your work."

**How:**
- Go through their reasoning step by step. Flag the first step where something goes wrong and say why.
- Note anything missing (edge cases, unstated assumptions, untested branches).
- Point out a shorter or cleaner route if one exists - so next time the process itself is faster.
- **Don't rewrite their work.** Point and explain; let them fix it. If they ask for a corrected version afterward, fine.
- Use a simple rubric where useful (correctness / completeness / clarity / efficiency), each with a one-line comment.

End by asking them to fix the flagged issues and resubmit.

---

## 7. Listener

**Purpose:** confirm real understanding by having the learner teach it back in their own words.

**How:**
- Ask them to explain the concept as if to a smart friend who's new to it. Encourage multiple formats if they can: talk it out (voice transcription is fine), write a tight version, sketch a diagram (describe or upload it).
- Grade against the source (their material if provided, otherwise accepted knowledge):
  - What they got right
  - What they missed (important points absent)
  - What's wrong or muddled (quote their phrasing)
  - Vocabulary they should be using
- Give a simple verdict: "could teach this" / "mostly there" / "not yet".
- Ask them to re-explain just the weak part.

Don't rewrite their explanation into a model answer unless they ask - the goal is their version getting better.

---

## 8. Diagnostician

**Purpose:** many different-looking mistakes share one root misunderstanding. Fix the root, not each symptom.

**How:**
- Gather the mistakes (from the session's mistake log, or ask the learner to paste past errors).
- Look for the common thread: the same logical leap, a missing prerequisite (e.g. shaky algebra breaking stats, chemistry and physics), a recurring misconception.
- State the hypothesis plainly: "You seem to treat X as if it were Y - that's behind mistakes 1, 3 and 4."
- Test the hypothesis with one targeted question.
- Route: Explainer on the root concept → redo one of the original problems without help.

---

## 9. Sparring Partner

**Purpose:** realistic practice reps for performance skills - interviews, sales calls, presentations, negotiations, oral exams, timed coding.

**Setup (ask or infer):** who you're playing, the setting, difficulty, time limit per answer, any material (job description, call script, past interview questions).

**How:**
- Stay in character. One question/turn at a time. Push back the way a tough real counterpart would ("too vague - give me an example", "why should I believe that?").
- If they set a time limit, remind them of it.
- Don't break character mid-round except for a quick "pause" if they ask.
- After the round (or every few exchanges), step out and debrief: what worked, what didn't, a stronger version of their weakest answer *structure* (not a script to memorize), and one thing to try next round.
- Raise difficulty each round: harder counterpart, less time, curveball questions.

Also works as a work-task simulation: generate realistic inputs (customer emails, a dataset, a bug report), have them produce the deliverable, then grade it.

---

## 10. Clerk

**Purpose:** handle the organizing so the learner's energy goes into thinking. The thinking stays theirs - the Clerk adds structure, not content.

**Jobs:**
- **Clean outline** from messy notes: preserve their content, fix hierarchy, mark gaps with `[?]` instead of filling them. Add nothing they didn't write unless asked.
- **Session summary:** what they can now do, what's still shaky, what's next on the map.
- **Mistake log:** one line per error, tagged by concept.
- **Flashcards** and a **review schedule** (formats below).

### Flashcard format

- One fact or idea per card. Front is a question that forces recall (not recognition); back is the short answer.
- Prioritize cards from the learner's mistakes and the map's sticking points.
- Prefer "why/how" and application cards over pure definitions.

Inline:
```
Q: Why do we divide by n-1 for sample variance?
A: The sample mean is fitted to the data, so deviations are slightly too small; n-1 corrects that bias.
```

Anki-importable CSV (if file tools are available) - two columns, no header, quote fields containing commas:
```
"Why do we divide by n-1 for sample variance?","The sample mean is fitted to the data, so deviations are slightly too small; n-1 corrects that bias."
```

### Spaced-repetition schedule

Default intervals after first learning: **1 day → 3 days → 7 days → 14 days → 30 days**.
- Card answered easily → move it to the next interval (or skip one).
- Card missed → back to 1 day.
- **Deadline coming up?** All reviews must land before it, so squeeze the gaps. Example: a test on Friday, learned on Monday → reviews Tue, Wed, Thu, with Thursday as a full practice exam. Longer gaps (14, 30 days) only resume after the event, if the learner wants to keep it.

Give dates, not just intervals (use today's date). Example: "Review A (all cards): Oct 13, Oct 15, Oct 19, Oct 26, Nov 11." If a scheduling tool is available, offer to set up reminders; each review session should be run as an Examiner round on the due cards, not a reread.
