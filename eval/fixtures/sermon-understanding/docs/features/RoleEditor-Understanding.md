# RoleEditor — Understanding

**Status**: `confirmed`
**Last Updated**: 2026-08-01
**Related Spec**: [RoleEditor.md](RoleEditor.md)
**Related TODO**: [RoleEditor-TODO.md](RoleEditor-TODO.md)

---

This file is the agent’s model of **feature shape** — identity and boundaries — so you can catch category mistakes before build. **The agent writes this file first** (status `draft`).

**Feature shape, not the spec.** Capture identity-defining detail.

*Too thin (drops shape):* “A role-specific view of the existing text editor.”

*Right size (shape):* Same framing plus identity detail.

*Wrong size (mini-spec):* Restating Core Behavior.

## What this is

A role-specific view of the existing BlockEditor. Same editing core (not a second engine). One continuous manuscript surface; chrome differs for this workflow.

## What this is NOT

*Bad example (do not write this):* “NOT freeform multi-window Desktop Mode — that is long-term in the spec.”

*Good example:* “NOT a freeform multi-window desktop OS.”

- NOT a second editor engine
- NOT a standalone document model

## Assumptions (needs user confirmation)

- [x] Same engine (confirmed)

## Confirmed with user

- 2026-08-01 — same editing core

## Instructions for AI Agents

Full procedure: workflow/understanding.md §4. Write this file first. Draft from the conversation. On update relocate trimmed contract. Set confirmed only after the user approves shape. Mermaid never on Understanding.

**Instructions for Humans**

You do not write this file from scratch. Confirm shape, not the full spec.
