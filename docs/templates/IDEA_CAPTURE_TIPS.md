# Tips for Capturing Your Idea

You do not need to be a software developer to use these templates well. Agents guess when details are missing — and guesses drift from what you actually want. The fix is not “learn to code first”; it is **describing the idea in plain language** using the kinds of details below.

Your answers feed [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md) — the file you (and the agent) review **before** building.

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

### 2. Scope — what it is and is **not**

This prevents the “brand-new feature” mistake when you meant a **variant** or **add-on**.

- Is this **new from scratch**, or a **new screen/mode** on something that already exists?
- What should we **explicitly not** build in this pass?

*Example:* “A separate UI layout for the existing text editor — **not** a second editor engine.”

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
2. Tell the agent (or write in Understanding) **two lists**:
   - **Similar:** what you want to borrow (layout, density, where the button lives, …)
   - **Different:** what your idea must not copy or must change
3. Get the image **into the repo** under `docs/features/assets/` and link it from your feature’s `-Understanding.md` so future sessions can open the same file.

#### Saving chat attachments to the repo

**Yes, when the agent can write files** — the goal is a real file in the repo, not a one-off chat image.

| How you provide the image | Can the agent save it? |
|---------------------------|-------------------------|
| **Save or drop the file** into `docs/features/assets/` yourself | Always works. Tell the agent the path; it links Understanding. **Most reliable.** |
| **Attach a file** from disk (or `@`-mention a path in the workspace) | Usually works. Agent copies or moves to `docs/features/assets/` with shell or file tools. |
| **Paste screenshot in chat** (no file on disk) | Agent **sees** the image (vision) but often **does not** get the original bytes. It may not be able to reproduce an identical PNG. Ask it to try; if it cannot, save the screenshot into `docs/features/assets/` yourself, then ask it to link + describe similar/different. |

In Cursor and similar IDE agents, the workspace **is** your repo — there is no separate “workspace copy” to pull from unless the tool exposes an attachment path. Prefer **file on disk in the project** over paste-only when you need a permanent reference.

**Agent should:** copy or move into `docs/features/assets/FeatureName-label.ext` when a source path exists; update **Visual references**; never leave the only copy in chat. If save is not possible, say so and ask the user to drop the file in `assets/`.

**Where files live:**

| Location | Use for |
|----------|---------|
| `docs/features/assets/FeatureName-short-label.png` | Reference for a specific feature |
| `docs/reference/visuals/` | General inspiration before a feature exists |

**Naming:** `FeatureName-what-it-is.png` (e.g. `RoleEditor-notion-focus-mode.png`).

**Example prompt:**

> Here’s a screenshot of Notion’s focus view. Save it under `docs/features/assets/RoleEditor-notion-focus.png`. In `RoleEditor-Understanding.md`, add a visual reference: **similar** = full-width text, minimal chrome; **different** = we keep our app’s Save button top-left, no floating slash menu.

**Why store in docs:** Chat attachments disappear. Files in the repo stay linked from Understanding and stay available to any agent with file or vision access later.

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

When you or the agent write `FeatureName-Understanding.md`:

| Your thinking | Understanding section |
|---------------|------------------------|
| Problem and purpose | **What this is** |
| What it is not | **What this is NOT** |
| Existing app pieces | **Relationship to existing work** |
| Steps and behavior | **How it should work** |
| Look, layout, references | **UI / UX intent** + **Visual references** |
| Things the agent guessed | **Assumptions** (you check boxes) |

Prompt the agent:

> Read `IDEA_CAPTURE_TIPS.md` and interview me briefly, then fill `[Feature]-Understanding.md`. Mark unknowns as assumptions.

Or answer the buckets yourself in chat, then:

> Turn my answers into `[Feature]-Understanding.md` using the template.

---

## “Good enough” is enough

- Rough answers beat silence.
- “I’m not sure about X” is useful — put it under **Assumptions**.
- You can confirm Understanding in five minutes and save days of wrong implementation.

---

## For AI agents

When the user describes a feature vaguely:

1. Read this file and [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md).
2. Ask **short, plain-language questions** from the buckets above — not a twenty-question form. Prioritize: scope (is/is not), UI, happy-path flow, relationship to existing work.
3. Write or update `-Understanding.md` with status `draft`. List gaps in **Assumptions**.
4. If the user provides screenshots, persist under `docs/features/assets/` (or `docs/reference/visuals/`): **copy/move from a workspace path** when the file is attached or `@`-mentioned; if only a pasted chat image (vision-only), ask the user to save into `assets/` or document similar/different from what you saw and note that a file copy was not available. Link in **Visual references** — see [Saving chat attachments](#saving-chat-attachments-to-the-repo).
5. If the user does not know stack or architecture, propose options **after** Understanding sections 1–4 are drafted, with a one-line rationale each.
6. Do not start implementation until the user confirms Understanding or explicitly waives review.

When the user **is** experienced, do not over-interview — still fill **What this is NOT** and **Relationship to existing work**; skip obvious questions.

---

## Related

- Workflows (chat → docs, etc.): [`USAGE.md`](USAGE.md)
- Understanding template: [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md)
- Setup: [`SETUP.md`](SETUP.md)
