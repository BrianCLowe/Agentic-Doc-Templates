# Rule Install — Agent Instructions

> Use when the user asks to bootstrap modular docs, install the rule, or set up agent instructions. **Ask before writing rule files** — unless `docs/ADT-settings.yaml` already records a decision for that tool (see below).
>
> **Dispatcher:** After the user confirms a tool, open **only** [`tools/<key>.md`](tools/README.md) and execute that playbook. Do not keep a second copy of install paths in this file.

## Settings file — remember answers

**Live file:** `docs/ADT-settings.yaml`  
**Example schema:** [`ADT-settings.example.yaml`](ADT-settings.example.yaml)

**Legacy:** If `docs/rule-install-status.yaml` exists and `ADT-settings.yaml` does not → migrate per [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) B0.1 first, then continue.

After the user answers for a **specific tool**, create or update `docs/ADT-settings.yaml` so future sessions do not re-ask for that tool.

### Tool keys (use exactly)

| Key | Tool | Playbook |
|-----|------|----------|
| `cursor` | Cursor | [`tools/cursor.md`](tools/cursor.md) |
| `grok-build` | Grok Build | [`tools/grok-build.md`](tools/grok-build.md) |
| `github-copilot` | GitHub Copilot (VS Code) | [`tools/github-copilot.md`](tools/github-copilot.md) |
| `claude-code` | Claude Code | [`tools/claude-code.md`](tools/claude-code.md) |
| `agents-md` | Root `AGENTS.md` (cross-tool) | [`tools/agents-md.md`](tools/agents-md.md) |
| `openclaw` | OpenClaw | [`tools/openclaw.md`](tools/openclaw.md) |
| `continue` | Continue.dev | [`tools/continue.md`](tools/continue.md) |
| `cline` | Cline | [`tools/cline.md`](tools/cline.md) |

### Status values

| Status | Meaning | Ask again? |
|--------|---------|------------|
| `installed` | Rule was installed at `path` | No — unless install file is missing, or user asks to reinstall/sync |
| `declined` | User chose not to install for this tool | No — unless user explicitly asks to install for that tool |

Optional fields: `recorded` (YYYY-MM-DD), `path`, `note`, `customized` (true only if user hand-edited pack-managed rule bodies — sync asks before overwrite).

### Optional rules (`optional_rules` in the same file)

| Key | Meaning |
|-----|---------|
| `template-update-check` | Ping for newer Agentic Doc Templates — see [`TEMPLATE_UPDATE_CHECK.md`](TEMPLATE_UPDATE_CHECK.md); default `upstream.check_mode: always` (interval optional) |
| `doc-roles` | Optional playbook roles — see [`roles/README.md`](roles/README.md). **Not always-on.** Installed per tool file (`.cursor/agents/`, `.grok/agents/`, …). |

| Status | Meaning |
|--------|---------|
| `enabled` | User opted in (bootstrap Step 3p preference batch or explicit ask). When installing/refreshing a tool, that tool’s `tools/<key>.md` also installs matching optional artifacts. |
| `declined` | User opted out — do not install; do not re-ask unless they request it. |
| *(missing / unset)* | **Not** a silent no. Briefly explain the option and ask once; then record `enabled` or `declined`. |

### Sync mode (`sync.mode`)

| Mode | Meaning |
|------|---------|
| `auto` | Pack sync applies recommended live updates + local post-sync hygiene commits without mid-sync quizzes — see [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md). Still asks once for brand-new unset `optional_rules.*`. Pre-sync dirty tree still hard-stops ([`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) A0) |
| `auto-all` | Same as `auto`, and also enable + install unset `optional_rules.*` without asking (never re-enable `declined`) |
| `choose` | Present optionals each sync; suggest commits, ask before committing |
| *(missing / unset)* | Ask once (bootstrap Step 3p or first sync) — do not silent-default |

If `optional_rules.template-update-check` is missing: under **`sync.mode: auto-all`** enable + install (default `check_mode: always`); otherwise bootstrap should have asked — if you are mid–rule-install (or finishing a template sync) and it is still unset, ask once using the Step 3p **B** wording, then record `enabled` or `declined`.

If `optional_rules.doc-roles` is missing: under **`sync.mode: auto-all`** enable + install adapters for each `tools.*.status: installed` tool that supports them; otherwise ask once using bootstrap Step 3p **C** for **any** rule-install or template-sync pass — not only when installing Cursor/Grok/Claude. Explain what “yes” means for each installed tool (agents-folder adapters where supported; Copilot/OpenClaw/etc.: no adapter files — parent follows `roles/*.md` in-session). Then record `enabled` or `declined`. Do **not** skip the ask because the current tool’s Install row is None.

If `orchestrator.git.mode` is missing mid-sync: **B0.6 always ask** (even under `auto-all`) — never invent `current-push` or silent-write.

## Before asking

1. Check whether `docs/Master_Index.md` exists (if not, follow [`BOOTSTRAP.md`](BOOTSTRAP.md) first — doc structure before rules).
2. Read **`docs/ADT-settings.yaml`** if it exists (migrate legacy status files first if needed).
3. For each tool you would prompt about, check its entry:
   - `installed` and install file still exists → skip; mention it is already set up.
   - `installed` but file missing → tell the user and offer reinstall (do not skip silently).
   - `declined` → skip unless the user explicitly requested install for that tool.
   - No entry → eligible to ask.
4. Check **only** destinations named in the relevant `tools/<key>.md` for unsettled tools (plus `AGENTS.md` / `CLAUDE.md` if present). Do **not** glob the repo for rule-like files.
5. State which tool you **think** the user is on and why — only if evidence is clear. If uncertain, say so.
6. **Ask the user** only for tools without a settled status:
   - Install the modular documentation rule for **[tool]**?
   - Other tools they use on this repo? (each gets its own entry and playbook)
   - If target file already has content: merge, append a section, or skip?

Do not proceed until they confirm for each tool you are installing.

## Why ask first

- You may **misidentify the current tool** (Cursor vs Copilot vs Grok Build, etc.).
- The user may **use multiple tools** on the same repo. Each tool uses a **different path** — they coexist without conflict.
- Existing instruction files may already contain **custom content** you must not overwrite.

## Install / refresh (dispatch)

For **each** confirmed tool (or each `tools.*.status: installed` when refreshing on sync):

1. Open **`docs/templates/agent/tools/<key>.md` only**.
2. Execute that playbook end-to-end (modular rule → optional update-check if enabled → optional doc-roles if enabled and that tool supports them).
3. Update `docs/ADT-settings.yaml` immediately (`status: installed`, `path`, `recorded`).
4. Stop for that tool — do not open other `tools/*.md`.

On **template sync** `rules` refresh: overwrite pack-managed installs **without asking** unless that tool has `customized: true`.

### After the user answers no

Set `status: declined`, `recorded`, optional `note`. Do not record tools you did not ask about.

### Explicit overrides

Always honor direct requests, even when status is `declined`:

- "Install the rule for Copilot" → open [`tools/github-copilot.md`](tools/github-copilot.md), install, set `installed`.
- "Reset rule install status" / "Ask me again about Cursor" → remove or update that tool's entry, then ask.
- "Set sync to auto" / "Set sync to auto-all" / "Set sync to choose" → update `sync.mode` in `ADT-settings.yaml`.

## Multi-tool setups (no conflict)

Installing for one tool **does not remove or replace** another tool's files. Record **each tool separately**.

`AGENTS.md` (`agents-md`) plus tool-specific files means redundant context — acceptable when the user wants cross-tool coverage.

## Shared install rules

- **Never overwrite** an existing instructions file without showing what will change and getting confirmation — **except** template-sync refresh of pack-managed modular / timescale / build-verify rule bodies for `installed` tools that are not `customized: true`.
- If merging into `copilot-instructions.md`, `CLAUDE.md`, or `AGENTS.md`, **append** a clearly labeled section; do not delete existing sections. On refresh, replace only the pack-owned Documentation workflow / timescale / build-verify sections.
- If the modular rule is **already present** at the target path, set status to `installed` if missing from yaml — do not re-install blindly.
- Do not edit files under `docs/templates/` except when copying **from** them.
- After install, tell the user which file(s) were created or updated.
- Optional artifacts (`template-update-check`, `doc-roles`) are installed **inside** each tool playbook when those optional_rules are `enabled` — not from a second global table in this file.

## Suggested prompt to the user

> I found `docs/templates/agent/tools/` with per-tool install playbooks. You're likely using **[tool]**.
>
> On disk: [existing install paths or none].  
> Settings (`docs/ADT-settings.yaml`): [Cursor: installed | Grok Build: not asked yet | …].  
> Sync mode: [auto | auto-all | choose | not asked — see bootstrap Step 3p].  
> Template update checks: [enabled | declined | not asked — see bootstrap Step 3p].  
> Optional doc roles: [enabled | declined | not asked — see bootstrap Step 3p].  
> Orchestrator git: [branch-pr-squash | branch-pr | … | not asked — see bootstrap Step 3p / B0.6].
>
> Install the modular docs rule for **[tool]**? (I won't ask again for that tool after you answer.)  
> If you also use other agents on this repo, say which — each gets its own `tools/<key>.md` pass.

## Example user prompts

- "Bootstrap modular docs in this project."
- "Install the modular documentation rule for Grok Build."
- "Set up the agent rule — I use Cursor here but Copilot at work." → dispatch `cursor`, then ask about `github-copilot` if no entry yet.

## Related

- Tool playbooks: [`tools/README.md`](tools/README.md)
- Settings example: [`ADT-settings.example.yaml`](ADT-settings.example.yaml)
- Optional doc roles: [`roles/README.md`](roles/README.md)
- Doc structure bootstrap: [`BOOTSTRAP.md`](BOOTSTRAP.md)
- Updating live docs from templates: [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
- Cheap update ping: [`TEMPLATE_UPDATE_CHECK.md`](TEMPLATE_UPDATE_CHECK.md)
- Human TOC: [Using With AI Agents](../help/USING_WITH_AGENTS.md)
