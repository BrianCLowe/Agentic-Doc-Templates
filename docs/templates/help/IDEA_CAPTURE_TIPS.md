# Tips for Capturing Your Idea

You do not need to be a software developer to use these templates well. Agents guess when details are missing — and guesses drift from what you actually want. The fix is not “learn to code first”; it is **describing the idea in plain language** using the kinds of details below.

Your answers in chat feed the agent's draft of [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md) — the file **the agent writes first** and **you confirm for shape / guardrails** (is / is not + Assumptions) before building. That is **not** a full-spec review. You describe the idea; you do not need to write this file yourself.

---

## Recommended: export idea chats into `docs/reference/`

This pack is built around a simple habit:

1. Work out ideas in a **chat** (Grok.com, ChatGPT, Claude web, etc.) — one thread per aspect is fine.
2. **Export** each conversation to markdown (or paste the full thread).
3. Drop the files into **`docs/reference/`** (often several — even ten or more — as you explore different parts of an app or game).
4. Ask your coding agent to **build or update** live docs from those files (Understandings first; Document Map + stubs as needed).

**Simple ask:**

> Build or update the live docs from `docs/reference/`.

Agents are instructed to keep reference files and to **split** unlike feature identities without you putting that in the ask.

**Why exports beat a polished design doc for this pack:** messy threads keep your **whys**, rejected alternatives, motives, and half-formed constraints — the intent that gets sanded off when you rewrite into a clean PRD. Agents build better Understandings from that raw trail; you still confirm **is / is not**, not every contract detail.

You do **not** need to rewrite chats into a design doc first. Polished design docs / PRDs are still welcome in `docs/reference/` — when both exist, keep the **chat exports too** and point the agent at both.

**Save lasting copies under `docs/reference/`** (e.g. `docs/reference/combat-feel-chat.md`, `docs/reference/inventory-thread.md`). That folder is for source material — not living Understanding/spec/TODO files.

### Optional: browser chat exporter

Any method that gets a **full markdown (or text) transcript** into `docs/reference/` is fine — copy-paste, native export, or an extension.

One option that supports Grok, ChatGPT, Claude, Gemini, and others with **Markdown** export: **[AI Exporter](https://saveai.net/)** (browser extension). Prefer **Markdown** over PDF for agent use. **Why this one is recommended here:** it **timestamps** messages, so when you drop **several conversation exports** into `docs/reference/`, the agent can order decisions **across those threads** and treat later ones as superseding earlier ones. This pack does **not** require it — use whatever you trust and already have; if your exports lack timestamps, say which file should win when they conflict.

### Split when identity differs *(agent duty — not part of your ask)*

One Understanding / Document Map row = **one finished-feature identity**. If source material covers two things that do **different jobs**, agents should create **two rows** and two file sets without waiting for you to say “split.” You only need to correct them if they still merged unlike ideas.

Day-to-day patterns: [`USAGE.md`](USAGE.md).

---

## You do not need to pick a tech stack

If you do not know React, Python, databases, or “the cloud,” that is fine. Describe:

- **What** the app or feature should do for a person using it
- **What it looks and feels like** (even roughly)
- **What it connects to** (e.g. “like the editor we already have,” “like Google Docs sharing”)
- **Constraints** (phone vs desktop, must work offline, must be simple)

A good agent can **propose** a stack from that and explain why. Your job is the product picture; stack choice can come after Understanding is clear.

---

## Details that reduce drift

Think in these buckets. You do not need every answer on day one — fill gaps over one short conversation with the agent.

### 1. Problem and purpose

- Who is this for? (you, your team, customers, players, …)
- What problem does it solve or what job does it do?
- What does success look like in one sentence?

*Example:* “Writers need a distraction-free mode that hides everything except the text and a save button.”

### 2. Scope — what it is and is **not** *(when complete)*

This prevents the “brand-new feature” mistake when you meant a **variant** or **add-on**. Describe the **finished** feature’s identity — not what you are skipping in the current sprint.

- Is this **new from scratch**, or a **new screen/mode** on something that already exists?
- What **kind of thing** is it *not* (wrong category), even after it is fully built?
- How should it **feel as a surface** when done? (e.g. one continuous document vs separate panes; same engine vs a second system)
- Phased / later work for the *same* feature → tell the agent for the **TODO** or **spec**, not for **What this is NOT**.

*Example:* “A separate UI layout for the existing text editor — **not** a second editor engine.”  
*Example (surface):* “Feels like one manuscript; scene breaks are visual seams — **not** jumping between separate editor windows.”  
*Not for Understanding NOT:* “Desktop Mode comes later” — that is a TODO / roadmap item if it is still part of this feature’s destination.

### 3. UI appearance

You do not need a design degree. Any of these help:

- “Single column, big text, dark background”
- “Same toolbar as the main screen but without the side panel”
- “Like [app or website you know] but without [part you dislike]”
- List of **on-screen elements**: buttons, menus, fields, labels

*Example:* “Top bar with title and Save. Main area is full-width text. No sidebar. Footer shows word count.”

### Visual references (screenshots)

If your agent supports **images** (Cursor, ChatGPT, Claude, Grok, etc.), screenshots are one of the best ways to explain UI.

**What to do:**

1. Capture a **similar** site or app — not necessarily identical, just “in the ballpark.”
2. Tell the agent **two lists** (in chat is fine — the agent puts them on the **spec**):
   - **Similar:** what you want to borrow (layout, density, where the button lives, …)
   - **Different:** what your idea must not copy or must change
3. Get the image **into the repo** under `docs/features/assets/` and link it from your feature’s **spec** (`FeatureName.md` **Visual references**) so future sessions can open the same file. Understanding stays shape-only (is / is not) — no screenshot table there.

#### Saving chat attachments to the repo

**Yes, when the agent can write files** — the goal is a real file in the repo, not a one-off chat image.

| How you provide the image | Can the agent save it? |
|---------------------------|-------------------------|
| **Save or drop the file** into `docs/features/assets/` yourself | Always works. Tell the agent the path; it links the **spec**. **Most reliable.** |
| **Attach a file** from disk (or `@`-mention a path in the workspace) | Usually works. Agent copies or moves to `docs/features/assets/` with shell or file tools. |
| **Paste screenshot in chat** (no file on disk) | Agent **sees** the image (vision) but often **does not** get the original bytes. It may not be able to reproduce an identical PNG. Ask it to try; if it cannot, save the screenshot into `docs/features/assets/` yourself, then ask it to link + describe similar/different on the **spec**. |

In Cursor and similar IDE agents, the workspace **is** your repo — there is no separate “workspace copy” to pull from unless the tool exposes an attachment path. Prefer **file on disk in the project** over paste-only when you need a permanent reference.

**Agent should:** copy or move into `docs/features/assets/FeatureName-label.ext` when a source path exists; update the **spec** **Visual references**; never leave the only copy in chat. If save is not possible, say so and ask the user to drop the file in `assets/`.

**Where files live:**

| Location | Use for |
|----------|---------|
| `docs/features/assets/FeatureName-short-label.png` | Reference for a specific feature |
| `docs/_shared/assets/ComponentName-short-label.png` | Reference for a shared component UI |
| `docs/reference/visuals/` | General inspiration before a feature exists |

**Naming:** `FeatureName-what-it-is.png` (e.g. `RoleEditor-notion-focus-mode.png`).

**Example prompt:**

> Here’s a screenshot of Notion’s focus view. Save it under `docs/features/assets/RoleEditor-notion-focus.png`. In `RoleEditor.md` **Visual references**, add: **similar** = full-width text, minimal chrome; **different** = we keep our app’s Save button top-left, no floating slash menu.

**Why store in docs:** Chat attachments disappear. Files in the repo stay linked from the **spec** and stay available to any agent with file or vision access later.

**Your own app:** Screenshots of *your* existing UI also belong here — “make the new screen look like this panel, not like the whole app.”

---

### 4. Interactions

What can the user **do**, and what happens?

- Click / tap / drag / keyboard shortcuts
- What is **disabled** or **hidden** in certain states?
- Single-click vs double-click, confirm dialogs, undo

*Example:* “Save button writes immediately. Esc exits focus mode and returns to the normal editor.”

### 5. Flow (step by step)

Walk through the **happy path** like a short story:

1. User opens the app / feature from where?
2. Then they do …
3. Then they see …
4. They finish when …

Also worth one line each:

- **First time** vs **returning** user (empty state vs existing content)
- **Wrong input** — what should happen?
- **Cancel or back** — where do they land?

*Example:* “From document list → open doc → click Focus Mode → edit → Save or Esc → back to normal view.”

### 6. Usability and feel

- Speed: must it feel instant, or is a short loading OK?
- Errors: show a message, retry, or silent fail?
- Accessibility: large text, keyboard-only, screen reader — anything mandatory?
- Devices: desktop only, phone, both?

*Example:* “Loading spinner if save takes more than a second. Error toast if save fails — never lose text.”

### 7. Data and content (plain language)

No schema required — describe **stuff**:

- What does the user type, upload, or select?
- What gets saved, and where should it “live” conceptually? (this document, this project, my account)
- Who can see or edit it?

*Example:* “Same document as normal editor — focus mode is only a view, not a copy.”

### 8. Constraints and connections

- Must match an **existing** part of the app (name it)
- Legal, privacy, or “must not send data externally”
- Timeline: MVP vs later

*Example:* “Must reuse current login and document storage — no new account system.”

---

## Vague vs clearer (same idea)

| Vague | Clearer |
|-------|---------|
| “Add a focus mode” | “Full-screen view of the **existing** editor; hide nav and sidebar; keep Save and Esc to exit.” |
| “Make it like Notion” | “Block-based notes with a + button to add blocks; **only** title + paragraph for v1.” |
| “User dashboard” | “After login, list of my projects with name + last edited date; click opens project; button ‘New project’ top right.” |
| “Better settings” | “Settings page: toggle dark mode, dropdown for language (EN/ES), Save at bottom.” |

Clearer does not mean longer — it means **boundaries** and **concrete screens/steps**.

---

## How this maps to your docs

The **agent** drafts `FeatureName-Understanding.md` (or `_shared/ComponentName-Understanding.md`) from your conversation. You **review shape / guardrails** — not a full spec. You do not need to write the file yourself.

| Your thinking (in chat) | Where it lands |
|-------------------------|---------------|
| What *kind of thing* it is (identity, metaphors, defining constraints, brief “feels like,” product surface) | Understanding **What this is** |
| Wrong category / product surface / identity (not “not built yet”) | Understanding **What this is NOT** |
| Existing app pieces | Understanding **Relationship to existing work** |
| Things the agent guessed | Understanding **Assumptions** |
| Rough happy path / flows | **spec** **Behavior** *(not on Understanding)* |
| Module/API architecture, durable contract | **spec** *(not on Understanding)* |
| Screenshots + similar/different | **spec** **Visual references** |
| A few coarse “done” outcomes | **spec** **Acceptance** *(not a TODO twin)* |
| Work breakdown (target architecture — not interim staging) | **TODO** |

Product-defining surface (“feels like one document”) is **shape**. Module diagrams, APIs, full behavior, and the work backlog belong in the **spec** and **TODO** after you confirm shape. Agents should plan the confirmed target without you reminding them.

Prompt the agent:

> Read `IDEA_CAPTURE_TIPS.md`, interview me briefly if needed, then **draft** `[Feature]-Understanding.md` for my review of **shape** (is / is not). Mark unknowns as assumptions.

If you already answered the buckets in chat:

> Turn my answers into a **draft** `[Feature]-Understanding.md` using the template — I'll confirm shape, not the full spec.

---

## “Good enough” is enough

- Rough answers in chat beat silence — the agent turns them into a draft Understanding.
- The **whole** messy thread beats a polished one-page rewrite when you have it ([Recommended: export idea chats](#recommended-export-idea-chats-into-docsreference)).
- “I’m not sure about X” is useful — the agent puts it under **Assumptions** for you to confirm.
- You can review **shape** in a few minutes — you are not signing off the full contract here.

---

## For AI agents

When the user describes a feature vaguely:

1. Read this file and [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md). If they pointed at `docs/reference/` chat exports, **read those first** — prefer raw threads over polished-only summaries. When exports include **timestamps**, use them to order decisions **across different conversation files**: newer timestamps supersede older ones unless the user says otherwise.
2. Ask **short, plain-language questions** from the buckets above — not a twenty-question form. Prioritize: identity (is / is not *as a finished feature*), product surface when relevant, and relationship to existing work. Do not put phased or deferred work under **What this is NOT**.
3. Write or update `-Understanding.md` with status `draft` — **only** What this is / is NOT, Relationship, Assumptions, Confirmed notes. Keep identity-defining user detail **including product-defining surface/architecture**; do not pad into a mini-spec. No How it should work, UI/UX, Visual references, or Done when on Understanding. List gaps in **Assumptions**. Size TODOs for that target shape (agent timescale). On updates: re-check that stem’s TODO vs code/spec; **uncheck** anything that no longer matches; relocate trim overflow into the spec.
4. Tell the user confirmation is for **shape / guardrails**, not a full spec review. After they confirm, **graduate** durable contract content to the spec (`Feature_Spec_Template.md`) — Decisions, module/API architecture, Acceptance, shared Maturity. Spec may hold detail that was never in Understanding. Do not ask them to remind you to plan ambitiously.
5. If the user provides screenshots, persist under `docs/features/assets/` or `docs/_shared/assets/` (or `docs/reference/visuals/`): **copy/move from a workspace path** when the file is attached or `@`-mentioned; if only a pasted chat image (vision-only), ask the user to save into `assets/` or document similar/different from what you saw and note that a file copy was not available. Link in the **spec** **Visual references** — see [Saving chat attachments](#saving-chat-attachments-to-the-repo).
6. If the user does not know stack or architecture, propose options **after** Understanding shape sections are drafted, with a one-line rationale each — durable choices land in the **spec**.
7. Do not start implementation until the user confirms Understanding **shape** or explicitly waives review.
8. End sessions by updating TODO **Current focus** ([`workflow/todos.md`](../agent/workflow/todos.md) §5.1). Preference corrections during polish → same-turn spec **Decisions** ([`workflow/decisions.md`](../agent/workflow/decisions.md)), not deferred to wrap-up.

When the user **is** experienced, do not over-interview — still fill **What this is NOT** and **Relationship to existing work**; skip obvious questions.

---

## Related

- Workflows (chat → docs, etc.): [`USAGE.md`](USAGE.md)
- Understanding template: [`../templates/Feature_Understanding_Template.md`](../templates/Feature_Understanding_Template.md)
- Setup: [`SETUP.md`](SETUP.md)
