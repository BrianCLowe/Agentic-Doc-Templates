# VideoGeneration

**Related Understanding**: [VideoGeneration-Understanding.md](VideoGeneration-Understanding.md)
**Related TODO**: [VideoGeneration-TODO.md](VideoGeneration-TODO.md)

## Overview

Operator-facing export: turn a manuscript into a short video. Domain encode exists; humans must still be able to run it.

## Architecture / Contract

- **Owns**: encode job, export presets
- **Does not own**: editing canvas

## Behavior

- `encode(manuscript) -> mp4` in the library.
- Operators run export from a control surface (UI or CLI).

## Acceptance

- [ ] Library can encode a manuscript to mp4
- [ ] Operator can run the happy-path export without calling the library from a REPL
