---
name: pack-release-tag
description: Push the Agentic Doc Templates pack release tag after a version is on main. Use when the user says merged, push the tag, push the last tag, tag the release, or publish the GitHub Release. Checks pack-version against remote v* tags with a fixed command sequence. Do not search the repo for the tagging procedure.
---

# Pack release tag

Tag the pack version that is already on `main`. This file is the procedure. Do not open `CHANGELOG.md`, `release.yml`, or past tags to rediscover it.

## Check every time

Run these three commands. Do not add a search.

```bash
git fetch origin main
git show origin/main:docs/templates/VERSION
git ls-remote --tags origin 'v*'
```

`pack-version:` in that VERSION file is `X.Y.Z`. The tag name is `vX.Y.Z`.

Compare that name to the remote tag list:

- `refs/tags/vX.Y.Z` already exists → say so and stop. Do not move the tag.
- It is missing → push it (below).
- An older `X.Y.Z` has no tag → name that gap in one line. Do not put the older tag on the current tip. Tag an older version only when the user asks, and only on a commit whose `docs/templates/VERSION` equals that version.

## Push

`origin/main` must already contain the bump. The tip's `pack-version` must equal the tag you are about to create. The release workflow rejects a mismatch.

```bash
git tag vX.Y.Z origin/main
git push origin vX.Y.Z
```

The tag is lightweight. Do not annotate it. Do not force-push. Do not bump `VERSION` in this step.

Pushing the tag starts `.github/workflows/release.yml`, which builds `agentic-doc-templates-X.Y.Z.zip` from `docs/templates/` and publishes the GitHub Release.

## Tag exists, Release does not

Do not retag. Tell the user to run **Actions → Release → Run workflow** and enter the existing tag.
