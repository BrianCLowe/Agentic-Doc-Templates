# [Project Name] — Tooling

> Never edit this template unless the user asks you to. Live file: `docs/Tooling.md` (copy from this template at bootstrap or when first needed).

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md) - [workflow/tooling.md](templates/agent/workflow/tooling.md) Section 11

---

Machine / workflow tools needed to **develop this project** — not package dependencies (`package.json`, `Cargo.toml`, NuGet, etc.). Those stay in the usual lockfiles and install via the project’s normal package manager.

**Why this exists:** One short, accurate list of the tools this project needs and the services the running app calls.

**Table style:** **Why** = one line. **Install hint** = one command or a link to official docs — not a tutorial.

---

## What belongs here

| Include | Do not include |
|---------|----------------|
| CLIs, SDKs, runtimes, editors/engines required to build or run | Libraries listed in package manifests |
| Optional helpers the team actually uses (formatters, DB clients) | One-off personal preferences unless the project depends on them |
| Verify commands that prove the tool is present | |

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
| [e.g. Python] | Runtime and tooling | [OS package manager] | `python --version` |
| [Add rows] | | | |

---

## Optional

| Tool | Why | Install hint | Verify |
|------|-----|--------------|--------|
| [e.g. Docker Desktop] | Local services | [vendor installer] | `docker version` |
| [Add rows] | | | |

---

## Services this app consumes *(omit section if none)*

External APIs and services the **running app** calls. Not CLIs or SDKs — those stay in Required / Optional. Not package dependencies. A successor should see this list without reading code.

Credential **name** only (the environment variable or vault entry name, never its value).

| Service | Why the app calls it | Credential name | Docs |
|---------|----------------------|-----------------|------|
| [e.g. Contoso Billing API] | [e.g. invoices] | [e.g. `CONTOSO_API_KEY`] | [vendor docs URL] |
| [Add rows or delete section] | | | |

---

## Instructions for AI Agents

Keep this file a description of the project's tools and services: [`workflow/tooling.md`](templates/agent/workflow/tooling.md). Do not invent tools or services. Do not write secrets.

## Instructions for Humans

- Keep this lean - only the tools and services this project actually uses.
- When you adopt a new tool the project depends on, add a row (or tell the agent to).
- When the app will call an external API, add a **Services this app consumes** row (or tell the agent). That list stays after the key is procured.
