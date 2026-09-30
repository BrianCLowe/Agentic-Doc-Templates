---
name: pack-release-tag
description: Push the Agentic Doc Templates pack release tag after a version is on main. Use when the user says merged, push the tag, push the last tag, tag the release, or publish the GitHub Release. Checks pack-version against remote v* tags with a fixed command sequence. Do not search the repo for the tagging procedure. Do not mention older versions that have no tag.
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

Compare only that name to the remote tag list. Ignore every other tag.

- `refs/tags/vX.Y.Z` already exists → say so and stop. Do not move the tag.
- It is missing → push it (below).

Do not name an older version that has no tag. Do not push one from this check.

## Push

`origin/main` must already contain the bump. The tip's `pack-version` must equal the tag you are about to create. The release workflow rejects a mismatch.

```bash
git tag vX.Y.Z origin/main
git push origin vX.Y.Z
```

The tag is lightweight. Do not annotate it. Do not force-push. Do not bump `VERSION` in this step.

Pushing the tag starts `.github/workflows/release.yml`, which builds `agentic-doc-templates-X.Y.Z.zip` from `docs/templates/` and publishes the GitHub Release.

## Tag exists, Release does not

This applies only to the current pack-version tag. Do not retag. Tell the user to run **Actions → Release → Run workflow** and enter the existing tag.

## Older tag

Not part of the check above. Pushing an older tag runs the Release workflow stored on that older commit. That publishes a Release and marks it the latest package.

Push one only when the user asks for that older tag. It must point at the commit whose `docs/templates/VERSION` equals that version, not at the current tip. Disable the Release workflow, push the lightweight tag, then enable the workflow again. If disable is rejected, do not push the tag.

```bash
gh workflow disable Release
git tag vX.Y.Z <commit>
git push origin vX.Y.Z
gh workflow enable Release
```

Confirm that tag has no GitHub Release and the previous latest release is unchanged.
