# Prompt: build "Coach", my personal study app

Copy everything below the line into an AI app builder (or a new Claude Code session) as the opening message.

---

## 1. What I want you to build

Build a personal study app for me, a Grade 12 student in the UAE. It is a study coach, tutor, question bank and planner in one, designed around how I actually behave, not how a perfect student behaves.

The single goal: **on every school day, I know exactly what to do next, I actually start, and I go to bed on time before exams.**

Build it as a **Progressive Web App (PWA)** that installs on my **iPad** and my **Samsung Android phone**, works offline for studying, and sends push notifications. Use simple, short English everywhere in the interface. Add an optional Gulf Arabic toggle for encouragement messages only.

## 2. About me (design for this)

**Schedule**
- School runs **Monday to Friday, 7:30 AM to 3:00 PM** (let me edit days and times, since Fridays can be shorter).
- I leave home around 6:30 to 6:40 AM and get home around 4:10 PM.
- I wake at 5:00 to 5:30 AM. Bedtime must be **9:30 to 10:00 PM** at the latest.
- I live in the UAE (Asia/Dubai time zone). Prayer and family dinner times move around, so every plan must be easy to shift by dragging a block.

**How I study best**
- **45-minute blocks**, 10-minute breaks, **phone in another room**, **hardest subject first**.
- I learn best by **answering questions, not rereading**: try first, then a hint, then the answer, then redo it myself.
- Short explanations with tricks and mnemonics stick best (e.g. "ADD means AWAY, REMOVE means TOWARD", "Strong wins").

**My traps (the app must actively fight these)**
- **TikTok**: "just one video" turns into an hour, especially in bed.
- **Naps that turn into hours**: a planned 20-minute nap became 5.5 hours and ruined my night and the next school day.
- **Re-planning instead of starting**: I ask for new plans, new apps and new tools instead of doing the first 10 minutes.
- **Stopping when it gets hard**: I say "idk" and want to quit.
- **Staying up too late before exams**, then sleeping through alarms.
- I get **tired after school**.

**My subjects and assessments**
- AP Calculus (differential equations, 7.8–7.9 and onwards), AP Chemistry (Ch 16: buffers, Henderson-Hasselbalch, titration), Biology (Topic 1: translation, gene regulation, cell specialization), Physics, English, AP Research (literature review), **SAT on November 7**.
- Teachers give **SBQs** (short / source-based quizzes) often, plus exams. Teachers email practice sheets and put materials on ClassKick and Teams.
- I also track **university scholarship deadlines** (e.g. SCO registration closes 11 Nov 2026) and I'm planning for Biomedical Science, then medicine.

## 3. Core features (MVP, in priority order)

### 3.1 Today screen (home)
- Shows **only what to do now**: one big card with the current block ("4:55–5:40 · Calc: exponential & logistic problems"), a **Start** button and a countdown.
- Below it, the rest of today as a simple timeline (time, subject, task, block type: study / break / meal / nap / sleep).
- A **"I'm behind" button** that rebuilds the rest of the day from the current time, keeps bedtime fixed, and cuts the lowest-priority blocks first (it tells me what it cut).
- A **"Start with 10 minutes" button** for when I'm stuck: shrinks the current task to one tiny step (e.g. "Answer Q1 only").
- Never show more than 3 choices at once.

### 3.2 Exam-aware planner
- I add assessments (subject, date, topics, type: SBQ / exam / AP / SAT, my confidence: weak / mid / solid).
- The planner works **backwards from each exam** and places 45-minute blocks across the days before it, putting weak topics and nearer exams first.
- Rules it must follow:
  - Night before an exam: **no new material after 9:15 PM**, review only.
  - Morning of an exam: 20–30 minutes of **missed questions and formulas only**.
  - Two exams the same day: split evenly, hardest first, and protect sleep.
  - If a test has a **retake/redo**, lower its priority (tell me).
- Weekly view so I can see the whole week's load (e.g. Wed Physics, Thu Bio + Calc, Fri Chem).

### 3.3 Notes-coverage audit (very important)
When I upload class notes (PDF or photos):
1. **Read the printed page numbers** and immediately tell me which pages are missing. Ask me to upload them.
2. **Read every page at high resolution**, including margins and between lines. Detect and list:
   - Handwritten teacher notes and formulas (e.g. a tiny "M×V = M×V" next to "Equivalence point").
   - Circled, starred, boxed, underlined words ("Define", "Calculate", "Label", "Graph").
   - "IMPORTANT NOTE" / "IMPORTANT EXAM NOTE" boxes, copied word for word.
   - **Crossed-out sections**: never drop them silently. Pull out the methods they use (e.g. mmol = M × mL, ÷ total volume) and keep those as items. Ask me if the teacher said they're excluded.
   - Hidden prerequisite formulas the notes use without explaining.
3. Build a **coverage checklist**: page · item · type · teacher signal · taught ☐ · quizzed ☐.
4. Before the app ever says "you're ready", it checks the list and shows me what was **not** covered.
5. After the exam, it asks "what came up that we didn't cover?" and saves the answer so it learns.

### 3.4 Question bank from my notes
- Generate questions **only from my uploaded material**, each tagged with the **page number** and topic.
- Clearly mark any answer choices or questions the app wrote itself versus ones copied from the file.
- Types: multiple choice, numeric (with tolerance), fill-in-the-blank, "explain why" (graded against my notes), label-the-graph (tap regions on a curve), reactions (e.g. HA + OH⁻ → ?).
- One question at a time, instant feedback, short explanation with the page reference.
- Filters: by topic, by page, **Missed only**.
- Mixed quizzes with a score and a level: not ready / nearly / ready.

### 3.5 Tutor mode (AI)
- Uses a "learning coach" method: ask before telling, one question at a time, hint → bigger hint → answer → "now you redo it without help".
- Tags its mode on screen: Explainer, Examiner, Socratic, Checker.
- Detects frustration ("idk", short angry replies) and responds by giving the answer simply, then an easy win question, and offers a break.
- Breaks every topic into small steps and shows how each small question links back to the real question in my notes.
- Keeps a **mistakes list** automatically.

### 3.6 Mistakes → flashcards → spaced review
- Every wrong answer becomes a flashcard (front/back, one fact each), highlighted as "your mistake".
- Spaced repetition schedule fitted to the exam date (squeeze reviews into the days before the exam).
- **"10-minute exam sheet"** button: generates a one-page memory sheet of everything for an exam: formulas, rules, mnemonics, exam sentences, and my mistakes at the top.
- Export flashcards as PDF and Anki CSV.

### 3.7 Check-ins and reminders (my "coach")
- Push notifications at block boundaries: start, mid-block nudge (optional), end + quick quiz question, break over.
- **Bedtime routine** at 9:15 PM: pack bag, alarm set across the room, phone out of the room, lights out by 9:30.
- **Wake-up** check-in with the morning plan and my missed questions.
- If I don't respond to a check-in, the next one is gentle and shrinks the task to 10 minutes. Never guilt-trip.
- No duplicate notifications. One clear list of upcoming check-ins I can edit or turn off.
- Later (phase 3): optional real phone calls via a voice service (e.g. Vapi or Twilio) at chosen times, with parent approval.

### 3.8 Anti-procrastination tools
- **Focus mode**: full-screen timer, "phone in another room" reminder, and a log of whether I started on time.
- **Nap guard**: naps are capped at 25 minutes, must have an alarm, and are blocked after 5:30 PM.
- **Re-planning guard**: if I ask to re-plan more than twice in an hour, the app says kindly "the plan is set, start the first 10 minutes" and shows only the Start button.
- **Late-night guard**: after bedtime, the app shows only "go to sleep" and how many hours of sleep I'll get if I sleep now.

### 3.9 Sleep
- Enter sleep times manually or import from Samsung Health (if possible) or a screenshot.
- Show sleep debt for the week and warn me before exam nights.
- Before an exam: "If you sleep now you'll get X hours" counter.

### 3.10 Study buddy chat
- Friendly peer tone, short messages, a little humour, celebrates wins ("8/10 from zero!").
- Calls out drifting kindly ("we've spent 40 minutes looking for apps").
- Remembers what I finished today.

### 3.11 Deadlines and admin
- Track assignments (e.g. AP Research literature review, extension status), homework, scholarship deadlines.
- Templates for short, polite emails to teachers (extension requests, missed exam / make-up requests), which I copy and send myself.

## 4. AI behaviour rules (apply everywhere)
- Never invent facts, page numbers or exam content. If unsure, say so.
- Every quiz question cites its source page.
- Don't agree with half-right answers; say exactly which part is right.
- Use simple English, short sentences, tables, and one emoji at most per point.
- Always end a study turn with either a question for me or "Next up" with 2–3 options, never both.
- Protect sleep over extra studying, every time.

## 5. Data model (starting point)
- **Subject**: name, colour, teacher, confidence.
- **Assessment**: subject, date, type, topics, retake available (y/n), status, result.
- **Material**: file, subject, pages present, pages missing.
- **CoverageItem**: material, page, text, type, teacher signal, taught, quizzed.
- **Question**: material, page, topic, type, prompt, choices, answer, tolerance, explanation, source (file / generated).
- **Attempt**: question, date, correct, time taken.
- **Flashcard**: question/mistake link, front, back, due date, ease.
- **Block**: date, start, end, type, subject, task, status (planned / started / done / skipped / cut).
- **CheckIn**: time, message, status (sent / answered / missed).
- **SleepLog**: date, bedtime, wake time, naps, score.
- **Deadline**: title, date, type, status.

## 6. Tech requirements
- PWA, mobile-first, works at phone width and on iPad; installable; offline for quizzes and flashcards.
- Light and dark themes.
- Push notifications (Web Push) with a reliable scheduler.
- AI: use the Anthropic Claude API with the latest Claude model for tutoring, question generation and the notes audit (vision for PDFs and photos). Keep API keys on the server, never in the app.
- PDF/photo handling: render pages at high resolution for the audit pass.
- Optional integrations: Google Calendar (put blocks and check-ins on my calendar), Google Drive (import notes).
- Privacy: I'm under 18. Store data privately, no social features, no ads, no selling data. Parent can be added as a viewer later.

## 7. Build phases
1. **Phase 1 (MVP):** Today screen, exam planner, question bank from uploaded notes with page citations, mistakes list, check-in notifications, bedtime routine.
2. **Phase 2:** Notes-coverage audit, tutor mode, flashcards with spaced repetition, 10-minute exam sheet, sleep log.
3. **Phase 3:** Study buddy chat, anti-procrastination guards, Google Calendar sync, optional phone-call check-ins.

## 8. Acceptance tests (the app is right when…)
- I upload a 17-page PDF that is missing pages 6, 12 and 16, and the app tells me within seconds which pages are missing.
- A tiny handwritten formula in a margin appears in the coverage checklist.
- A crossed-out worked example produces a checklist item for its method, not nothing.
- I press "I'm behind" at 5:16 PM and get a new plan that still ends at 9:30 PM and tells me what was cut.
- I answer 19 questions wrong, and they all appear under "Missed" and as flashcards the next morning, even after closing the app.
- After 9:30 PM, opening the app shows only the sleep screen.
- Every quiz question shows its page number.

## 9. First thing to do
Ask me 5 short questions to fill in anything missing (exact school days, my timetable, which device I use most, whether a parent should get updates, and which exam is next), then show me a clickable prototype of the Today screen before building the rest.
