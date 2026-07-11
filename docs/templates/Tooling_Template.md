# [Project Name] — Tooling

> Never edit this template unless the user asks you to. Live file: `docs/Tooling.md` (copy from this template at bootstrap or when first needed).

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md)

---

Machine / workflow tools needed to **develop this project** — not package dependencies (`package.json`, `Cargo.toml`, NuGet, etc.). Those stay in the usual lockfiles and install via the project’s normal package manager.

**Why this exists:** Clone the repo on a new machine and ask the agent to install tooling so you can keep working. Keep the list short and accurate.

---

## What belongs here

| Include | Do not include |
|---------|----------------|
| CLIs, SDKs, runtimes, editors/engines required to build or run | Libraries listed in package manifests |
| Optional helpers the team actually uses (formatters, DB clients) | One-off personal preferences unless the project depends on them |
| Verify commands that prove the tool is present | Full install manuals — link to official docs instead |

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

## After tools are installed

1. [e.g. Copy `.env.example` → `.env`]
2. [e.g. `npm install` / `pnpm install` / restore packages]
3. [e.g. How to start the app or open the editor]

Package installs are **not** listed as tools above — run them after required tooling is present.

---

## Instructions for AI Agents

- When the user says things like **“install tooling”**, **“set up this machine”**, or **“get this project working on a new PC”**: read **this file** (`docs/Tooling.md`), install **Required** tools for the current OS, then run **After tools are installed**. Ask before installing **Optional** unless the user said “everything.”
- Prefer the install hints in the table; fall back to official docs. Prefer non-interactive package managers when available (`winget`, `brew`, etc.).
- **Do not invent tools.** Only install what is listed (or what the user explicitly adds in this conversation — then update this file).
- After installing, run each **Verify** command and report pass/fail.
- If `docs/Tooling.md` is missing: create it from [`templates/Tooling_Template.md`](templates/Tooling_Template.md) by inferring from Project Profile / README / existing scripts — mark uncertain rows and ask the user to confirm before large installs.
- Keep this file updated when the project adopts a new required CLI or drops one.

## Instructions for Humans

- Keep this lean — only what a new machine needs.
- When you adopt a new tool, add a row (or tell the agent to).
- Simple ask on a fresh clone: *Install the project tooling for this machine.*
