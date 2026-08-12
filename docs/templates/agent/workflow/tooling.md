<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when installing machine tools or filling Project verify handoff.

# Tooling

## 11. Tooling *(new machine setup)*

Live file: **`docs/Tooling.md`** (from [`Tooling_Template.md`](../../Tooling_Template.md)).

Lists **machine / workflow tools** (CLIs, SDKs, runtimes, engines, profile-installed agent skills) — **not** package-manager dependencies.

When the user asks to install tooling / set up this machine / get the project working on a new PC:

1. Read `docs/Tooling.md`.
2. Install **Required** for the current OS (prefer user-level / non-interactive package managers).
3. Refresh PATH or use a new shell if needed; run every **Verify** command.
4. Install **Agent skills** rows if that section exists; new session may be required for skills to load.
5. Run **After tools are installed** (env files, package restore, start commands).
6. Report pass/fail. Install **Optional** only if asked (or “everything”). Ask before admin / large SDK installs.

Do not invent tools; update the file when the stack changes. No secrets in `Tooling.md`.

**Project verify (handoff):** Fill **`docs/Tooling.md` → Project verify (agent handoff)** with this repo’s real build/typecheck/container/engine commands when known. After code changes, agents follow [`Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) (core install with modular rules): run those commands (or proportional stack defaults), **fix failures**, and only then tell the user they can test. Build green ≠ operable product (see §5.3); both apply when both apply.

---
