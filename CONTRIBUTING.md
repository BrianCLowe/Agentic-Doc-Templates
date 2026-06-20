# Contributing to Agentic Doc Templates

Thanks for your interest in contributing! I use these templates daily in my own work, so I'm happy to improve them — but I want to keep the project focused and practical rather than letting it grow in too many directions at once.

## Ways to Contribute

Here are the most helpful ways to contribute:

- **Share how you're using the templates** and what workflows work well for you
- **Suggest improvements** to existing templates (clarity, structure, agent instructions)
- **Propose new templates** that fill a genuine gap
- **Report issues** when something doesn't work well with a specific tool (Cursor, Claude Code, etc.)

## How to Contribute

Since Issues are turned off, please use **Discussions** for most things:

- **Ideas, suggestions, and questions** — Start a new Discussion. This is the best place to talk about improvements, new template ideas, or how you're using the templates with different agents.
- **Pull Requests** — Welcome for small, focused improvements to existing templates. Please keep changes aligned with the current lightweight, modular style.

## What I'm Looking For

I'm more likely to merge contributions that:

- Improve clarity or reduce friction for both humans and agents
- Stay consistent with the current lightweight, modular approach
- Solve a real problem I've also run into

I'm more cautious about changes that significantly increase complexity or shift the overall direction of the project. I want to avoid ending up maintaining two versions (one public, one private that actually works for me).

If you're unsure whether something fits, just start a Discussion first — I'm happy to talk about it.

## Attribution

All contributions are accepted under the same [CC BY 4.0](LICENSE.md) license as the rest of the project.

Thanks again for helping make these templates better. I genuinely appreciate it.

---

## If you use this repo inside your project

**Recommended:** Copy only **`docs/templates/`** into your project. You do not need this repo's root files — your project keeps its own README and docs layout.

**If you cloned or copied the whole repository** into your project (or used "Use this template" and then merged into an existing app), three root files belong to the **template pack**, not your app:

| Root file | Relocate to |
|-----------|-------------|
| `README.md` | `docs/templates/agent/upstream/README.md` |
| `LICENSE.md` | `docs/templates/agent/upstream/LICENSE.md` |
| `CONTRIBUTING.md` | `docs/templates/agent/upstream/CONTRIBUTING.md` |

That keeps your project root for **your** README and metadata. Attribution and upstream license text stay in `upstream/` inside the template pack.

**Agent bootstrap:** Point your agent at [`docs/templates/agent/BOOTSTRAP.md`](docs/templates/agent/BOOTSTRAP.md) — Step 1 detects upstream root files and asks before moving them (including this file).

**Manual move:** Create `docs/templates/agent/upstream/` if needed, move the three files above, then write your own project `README.md` at the repo root.

Do **not** put `CONTRIBUTING.md`, `LICENSE.md`, or the template pack README at `docs/` root — only under `docs/templates/agent/upstream/` when you need them for attribution.