# [Project Name] — Tooling

> Never edit this template unless the user asks you to. Live file: `docs/Tooling.md` (copy from this template at bootstrap or when first needed).

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md) · [workflow/tooling.md](agent/workflow/tooling.md) §11

---

Machine / workflow tools needed to **develop this project** — not package dependencies (`package.json`, `Cargo.toml`, NuGet, etc.). Those stay in the usual lockfiles and install via the project’s normal package manager.

**Why this exists:** Clone the repo on a new machine and ask the agent to install tooling so you can keep working. Keep the list short and accurate.

**Table style:** **Why** = one line. **Install hint** = one command or a link to official docs — not a tutorial. Never put secrets, tokens, or license keys in this file.

---

## What belongs here

| Include | Do not include |
|---------|----------------|
| CLIs, SDKs, runtimes, editors/engines required to build or run | Libraries listed in package manifests |
| Optional helpers the team actually uses (formatters, DB clients) | One-off personal preferences unless the project depends on them |
| Agent skills / packs installed outside the repo (when the project depends on them) | Full install manuals — link to official docs instead |
| Verify commands that prove the tool is present | Secrets, API keys, license files |

---

## Host platforms

| Platform | Notes |
|----------|--------|
| Windows | [e.g. winget / scoop preferred] |
| macOS | [e.g. Homebrew] |
| Linux | [e.g. apt / pacman — distro notes] |

---

## Required

| Tool | Why | Install hint | Verify |
|------|-----|--------------|--------|
| [e.g. Node.js 20+] | Run app / scripts | [winget / brew / nvm] | `node -v` |
| [e.g. Git] | Version control | [OS package manager] | `git --version` |
| [Add rows] | | | |

---

## Optional

| Tool | Why | Install hint | Verify |
|------|-----|--------------|--------|
| [e.g. Docker Desktop] | Local services | [vendor installer] | `docker version` |
| [Add rows] | | | |

---

## Agent skills *(omit section if unused)*

Skills and packs that live in the **user profile** (not in git), e.g. `~/.grok/skills/`, `~/.codex/skills/`. Same idea as editor extensions — install per machine.

| Skill / pack | Host | Install location | Notes |
|--------------|------|------------------|--------|
| [e.g. generate2dsprite] | Grok / Codex | `~/.grok/skills/generate2dsprite/` | [upstream URL or install one-liner]; new agent session after install |
| [Add rows or delete section] | | | |

**Reload:** After installing or updating skills, start a **new agent session** so they load.

---

## After tools are installed

1. [e.g. Copy `.env.example` → `.env` — do not commit secrets]
2. [e.g. `npm install` / `pnpm install` / restore packages]
3. [e.g. How to start the app or open the editor]

Package installs are **not** listed as tools above — run them after required tooling is present.

**PATH:** After package-manager installs (especially on Windows), refresh PATH or open a **new shell**, then re-run **Verify** commands.

---

## Project verify *(agent handoff — required once filled)*

> **Agents:** Before telling the user they can test/run this project after code changes, run the commands below (see installed **Agent Build & Verify** rule / `docs/templates/agent/Agent_Build_Verify_Rule.mdc`). Fix failures; do not dump a raw “please build” on the user when these are runnable. Prefer the **smallest** row that covers the change; use **Full** when claiming the whole app/game works.

| Scope | When | Command(s) | Notes |
|-------|------|------------|--------|
| **Cheap / default** | Most code changes | [e.g. `npm run build` · `docker compose exec frontend bun run build` · `dotnet build` · UE editor compile target] | Must be runnable by the agent in this repo’s normal env |
| **Touched package** | Monorepo / multi-target | [e.g. build only backend or one game module] | Optional — use when faster and sufficient |
| **Full handoff** | “You can run the app/game” | [e.g. compose up + smoke · packaged build · Play-In-Editor load] | Optional if Cheap already equals full for this project |
| **Tests** *(optional)* | When CI/TODO requires | [e.g. `pytest` · Playwright profile] | Not a substitute for compile/typecheck when those exist |

**Examples by stack** *(replace with this project’s real commands — delete unused rows):*

| Stack | Typical cheap verify |
|-------|----------------------|
| Node / web | `npm run build` or `pnpm typecheck && pnpm build` |
| Dockerized app | `docker compose build <svc>` and/or `docker compose exec <svc> <build>` |
| Python | `ruff` / `mypy` / `pytest` as the repo already uses |
| .NET | `dotnet build` |
| Unreal | Project’s Build.bat / editor compile / documented UAT target |
| Unity / Godot | Project’s batch/CLI compile or documented play check |

Leave the table as placeholders until bootstrap/first implement fills real commands. Update when the stack changes.

---

## Machines *(optional — multi-machine teams)*

Track which boxes are set up so gaps are obvious. Delete this section if unused.

| Machine | Date | Required OK? | Notes |
|---------|------|--------------|--------|
| [e.g. desktop] | [YYYY-MM-DD] | | |
| [e.g. laptop] | | | |

---

## Instructions for AI Agents

- **“Install tooling” / “set up this machine” / “get this project working on a new PC”:** read **this file** (`docs/Tooling.md`) → install **Required** tools for the current OS → refresh PATH / new shell if needed → run every **Verify** → install **Agent skills** rows if present → run **After tools are installed** → report a pass/fail table. Install **Optional** only if the user asked for optional tools or “everything.”
- Prefer the install hints in the table; fall back to official docs. Prefer non-interactive package managers when available (`winget`, `brew`, etc.). Prefer **user-level** installs when possible.
- **Ask first** before admin-required installs, full Visual Studio / large SDKs, or anything that broadly rewrites system PATH beyond a normal package manager entry.
- **Do not invent tools.** Only install what is listed (or what the user explicitly adds in this conversation — then **add a row here** in the same session).
- **Do not** write secrets, tokens, or license keys into this file.
- If `docs/Tooling.md` is missing: create it from [`templates/Tooling_Template.md`](templates/Tooling_Template.md) by inferring from Project Profile / README / existing scripts — mark uncertain rows and ask the user to confirm before large installs.
- Keep this file updated when the project adopts a new required CLI/skill or drops one. Update **Machines** when the user cares about multi-machine status.

## Instructions for Humans

- Keep this lean — only what a new machine needs.
- When you adopt a new tool or agent skill the project depends on, add a row (or tell the agent to).
- Simple ask on a fresh clone: *Install the project tooling for this machine.*
