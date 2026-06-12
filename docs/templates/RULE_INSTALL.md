# Rule Install — Agent Instructions

> Use when the user asks to bootstrap modular docs, install the rule, or set up agent instructions. **Ask before writing rule files** — unless `docs/rule-install-status.yaml` already records a decision for that tool (see below).

## Status file — remember answers per tool

**Live file:** `docs/rule-install-status.yaml`  
**Example schema:** [`rule-install-status.example.yaml`](rule-install-status.example.yaml)

After the user answers for a **specific tool**, create or update `docs/rule-install-status.yaml` so future sessions do not re-ask for that tool.

### Tool keys (use exactly)

| Key | Tool |
|-----|------|
| `cursor` | Cursor |
| `github-copilot` | GitHub Copilot (VS Code) |
| `claude-code` | Claude Code |
| `continue` | Continue.dev |
| `cline` | Cline |
| `agents-md` | Root `AGENTS.md` (cross-tool section) |

### Status values

| Status | Meaning | Ask again? |
|--------|---------|------------|
| `installed` | Rule was installed at `path` | No — unless install file is missing, or user asks to reinstall/sync |
| `declined` | User chose not to install for this tool | No — unless user explicitly asks to install for that tool |

Optional fields: `recorded` (YYYY-MM-DD), `path`, `note`.

### Before asking

1. Read `docs/rule-install-status.yaml` if it exists.
2. For each tool you would prompt about, check its entry:
   - `installed` and install file still exists → skip; mention it is already set up.
   - `installed` but file missing → tell the user and offer reinstall (do not skip silently).
   - `declined` → skip unless the user explicitly requested install for that tool.
   - No entry → eligible to ask.
3. Only prompt for tools **without** a settled `installed` or `declined` record.

### After the user answers

Update `docs/rule-install-status.yaml` **immediately** for each tool decided in that conversation:

- **Yes, install** → perform install, set `status: installed`, `path`, `recorded`.
- **No** → set `status: declined`, `recorded`, optional `note` (e.g. "Uses Copilot only at work").

Do not record a decision for tools you did not ask about.

### Explicit overrides

Always honor direct requests, even when status is `declined`:

- "Install the rule for Copilot" → install (or merge), update status to `installed`.
- "Reset rule install status" / "Ask me again about Cursor" → remove or update that tool's entry, then ask.

## Why ask first

- You may **misidentify the current tool** (Cursor vs Copilot vs Claude Code, etc.).
- The user may **use multiple tools** on the same repo (e.g. Copilot at work, Cursor at home). Each tool uses a **different file** — they coexist without conflict.
- Existing instruction files may already contain **custom content** you must not overwrite.

Auto-installing without asking causes wrong-path installs and clobbered instructions. The status file prevents **repeated** prompts, not the initial ask.

## Before proposing an install

1. Check whether `docs/Master_Index.md` exists (if not, offer doc bootstrap first — see README bootstrap steps).
2. Read **`docs/rule-install-status.yaml`** and apply the rules above.
3. Scan for **existing** modular-docs rule installs on disk. Reconcile with the status file (fix stale `installed` if file was deleted).
4. State which tool you **think** the user is on and why — only if evidence is clear. If uncertain, say so.
5. **Ask the user** only for tools without a settled status:
   - Install the modular documentation rule for **[tool]**?
   - Other tools they use on this repo? (each gets its own entry and file)
   - If target file already has content: merge, append a section, or skip?

Do not proceed until they confirm for each tool you are installing.

## Install map (source → destination)

Copy from `docs/templates/`. Use the **same rule body** everywhere; only format and path differ.

| Tool key | Source template | Install to |
|----------|-----------------|------------|
| `cursor` | `Modular_Documentation_Rule.mdc` | `.cursor/rules/modular-documentation.mdc` |
| `github-copilot` | `Modular_Documentation_Rule.instructions.md` | `.github/instructions/modular-documentation.instructions.md` |
| `claude-code` | Rule body from `.mdc` (no Cursor frontmatter) | `.claude/rules/modular-documentation.md` or section in `CLAUDE.md` |
| `continue` | Rule body + frontmatter | `.continue/rules/modular-documentation.md` |
| `cline` | Rule body | `.clinerules/modular-documentation.md` or `.cline/rules/modular-documentation.md` |
| `agents-md` | Rule body | Section in root `AGENTS.md` titled `## Documentation workflow` |

Full tool notes: [Using With AI Agents](../USING_WITH_AGENTS.md).

## Multi-tool setups (no conflict)

Installing for one tool **does not remove or replace** another tool's files. Record **each tool separately** in `rule-install-status.yaml`.

A user who switches tools later may need an install for a **different** tool key — ask only for tools with no entry yet.

**Optional:** `AGENTS.md` plus tool-specific files means redundant context — acceptable. Do not duplicate into `AGENTS.md` unless the user wants cross-tool coverage (`agents-md` entry).

## Install rules

- **Never overwrite** an existing instructions file without showing what will change and getting confirmation.
- If merging into `copilot-instructions.md` or `CLAUDE.md`, **append** a clearly labeled section; do not delete existing sections.
- If the modular rule is **already present** at the target path, set status to `installed` if missing from yaml — do not re-install.
- Do not edit files under `docs/templates/` except when copying **from** them.
- After install, update the status file and tell the user which file(s) were created or updated.

## Suggested prompt to the user

> I found `docs/templates/` with the modular documentation rule templates. You're likely using **[tool]**.
>
> On disk: [existing install paths or none].  
> Status file: [Cursor: installed | Copilot: not asked yet | …].
>
> Install the modular docs rule for **[tool]**? (I won't ask again for that tool after you answer.)  
> If you also use other agents on this repo, say which — each gets its own file and status entry.

## Example user prompts

- "Bootstrap modular docs in this project."
- "Install the modular documentation rule for Copilot."
- "Set up the agent rule — I use Cursor here but Copilot at work." → install Cursor, record `cursor: installed`; ask separately about `github-copilot` if no entry yet.

## Related

- Status file example: [`rule-install-status.example.yaml`](rule-install-status.example.yaml)
- Doc structure bootstrap: project [README](../../README.md#bootstrap-a-new-project)
- Updating live docs from templates: [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
- Tool-specific details: [Using With AI Agents](../USING_WITH_AGENTS.md)
