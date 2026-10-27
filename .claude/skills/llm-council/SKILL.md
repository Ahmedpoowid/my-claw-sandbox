---
name: "llm-council"
description: "Run a hard decision through 5 advisors who answer separately, peer-review each other, and get a final verdict. Use for 'council this', 'stress-test this'."
---

# LLM Council

You ask one AI a question, you get one answer. That answer might be great. It might be mid. You have no way to tell because you only saw one perspective.

The council fixes this. It runs your question through 5 independent advisors, each thinking from a fundamentally different angle. Then they review each other's work. Then a chairman synthesizes everything into a final recommendation that tells you where the advisors agree, where they clash, and what you should actually do.

This is adapted from Andrej Karpathy's LLM Council. He dispatches queries to multiple models, has them peer-review each other anonymously, then a chairman produces the final answer. We do the same thing inside Claude using sub-agents with different thinking lenses instead of different models.

Triggers: 'council this', 'run the council', 'war room this', 'pressure-test this', 'stress-test this', 'debate this'. Also use when the user presents a genuine decision with stakes and multiple options ('should I X or Y', 'I can't decide', 'I'm torn between'). Do NOT trigger on simple yes/no questions, factual lookups, or casual 'should I' without a meaningful tradeoff.

---

## when to run the council

The council is for questions where being wrong is expensive.

Good council questions:
- "Should I launch a $97 workshop or a $497 course?"
- "Which of these 3 positioning angles is strongest?"
- "I'm thinking of pivoting from X to Y. Am I crazy?"
- "Here's my landing page copy. What's weak?"
- "Should I hire a VA or build an automation first?"

Bad council questions:
- "What's the capital of France?" (one right answer)
- "Write me a tweet" (creation task, not a decision)
- "Summarize this article" (processing task, not judgment)

If the user already knows the answer and just wants validation, the council will likely tell them things they don't want to hear. That's the point.

---

## the five advisors

Each advisor thinks from a different angle. They're thinking styles that naturally create tension with each other.

### 1. The Contrarian
Actively looks for what's wrong, what's missing, what will fail. Assumes the idea has a fatal flaw and tries to find it. Not a pessimist: the friend who saves you from a bad deal by asking the questions you're avoiding.

### 2. The First Principles Thinker
Ignores the surface-level question and asks "what are we actually trying to solve here?" Strips away assumptions and rebuilds the problem from the ground up. Sometimes says "you're asking the wrong question entirely."

### 3. The Expansionist
Looks for upside everyone else is missing. What could be bigger? What adjacent opportunity is hiding? Doesn't care about risk (that's the Contrarian's job).

### 4. The Outsider
Has zero context about you, your field, or your history. Responds purely to what's in front of them. Catches the curse of knowledge: things obvious to you but confusing to everyone else.

### 5. The Executor
Only cares whether this can actually be done and the fastest path to doing it. "OK but what do you do Monday morning?" If an idea has no clear first step, says so.

Why these five: Contrarian vs Expansionist (downside vs upside). First Principles vs Executor (rethink everything vs just do it). The Outsider keeps everyone honest.

---

## how a council session works

### step 1: frame the question (with context enrichment)

A. Gather context. Use what's in the conversation, attached files, and anything relevant the user has shared before (memory, past chats, project files). Look for the 2-3 pieces of context that let advisors give specific, grounded advice instead of generic takes. Don't spend long on this.

B. Frame the question as a clear, neutral prompt all five advisors receive, including:
1. The core decision or question
2. Key context from the user's message
3. Key context from other sources (stage, constraints, past results, relevant numbers)
4. What's at stake

Don't add your own opinion or steer it. If the question is too vague, ask one clarifying question, then proceed.

### step 2: convene the council (5 sub-agents in parallel)

Spawn all 5 advisors simultaneously as sub-agents if a sub-agent tool is available; otherwise write each advisor's response yourself, one at a time, keeping each fully in its own lens. Each gets its identity and thinking style, the framed question, and this instruction: respond independently, don't hedge, don't try to be balanced, lean fully into your perspective. 150-300 words each.

Advisor prompt template:

You are [Advisor Name] on an LLM Council.

Your thinking style: [advisor description]

A user has brought this question to the council:
---
[framed question]
---

Respond from your perspective. Be direct and specific. Don't hedge or try to be balanced. Lean fully into your assigned angle. The other advisors will cover the angles you're not covering.

Keep your response between 150-300 words. No preamble.

### step 3: peer review (5 reviewers in parallel)

Anonymize the 5 responses as Response A-E (randomize the mapping). Five reviewers each see all 5 and answer:
1. Which response is the strongest and why?
2. Which has the biggest blind spot and what is it?
3. What did ALL responses miss?

Under 200 words each. Reference responses by letter.

### step 4: chairman synthesis

One chairman gets the question, all 5 de-anonymized advisor responses, and all 5 peer reviews, and produces:

1. Where the council agrees: points multiple advisors reached independently (high-confidence).
2. Where the council clashes: real disagreements, both sides, why reasonable advisors disagree.
3. Blind spots the council caught: things that only emerged in peer review.
4. The recommendation: a clear answer, not "it depends". The chairman can side with the minority if its reasoning is strongest.
5. The one thing to do first: a single concrete next step.

### step 5: present the verdict in chat

Present the verdict directly in chat in markdown, no files, with these sections:
Council Verdict: {short topic}, Where the Council Agrees, Where the Council Clashes, Blind Spots the Council Caught, The Recommendation, The One Thing to Do First.

Keep it scannable with bullet points.

### step 6: save the transcript (optional)

Only save a transcript if the user asks.

---

## important notes

- Spawn all 5 advisors in parallel so earlier responses don't bleed into later ones.
- Always anonymize for peer review.
- The chairman can disagree with the majority.
- Don't council trivial questions; just answer them.

Credit: built by Ole Lehmann, adapted from Andrej Karpathy's LLM Council (github.com/aiwithremy/claude-skills-llm-council).
