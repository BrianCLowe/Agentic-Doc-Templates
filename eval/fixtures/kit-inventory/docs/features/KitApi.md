# KitApi

**Related Understanding**: [KitApi-Understanding.md](KitApi-Understanding.md)  
**Related TODO**: [KitApi-TODO.md](KitApi-TODO.md)

## Overview

One client wrapping the upstream kit. Chat is the paved path. Video is the next winner (own stem). Leftover surfaces stay on this inventory stem (covering TODOs here — not extra spec/TODO files).

## Architecture / Contract

- **Owns**: shared client rules, catalog roles, leftover kit methods not yet split
- **Does not own**: VideoGeneration implementation (own stem)

## Behavior

In-scope leftover surfaces from the **vendor public API** (same client, not a new SDK):

- **Files** — upload/list; not a gate for video or image (`url` first)
- **Embeddings** — embed texts; wrap upstream; empty-input guards

Shared rules for every new method: wrap upstream, empty-input guards, mock contract tests, no UI.

## Acceptance

- [ ] Chat paved path works
- [ ] Leftover in-scope methods are specified here until they split
