---
title: Validating your work
order: 2
---

# Validate the change, not just the build

**Every contribution must be validated before submission.** Reproduce the
original problem, establish what correct behavior looks like, and demonstrate
that your change achieves it without breaking the surrounding behavior.
Documentation-only contributions still need the relevant documentation checks.

## Start with the smallest meaningful check

During development, run the compilation, tests, and static checks for the
affected module. For a shared implementation change:

```sh
./gradlew :core:compileJava :core:test :core:immaculateCheck :core:checkstyle
```

Replace `:core` with the module you changed, or combine affected modules in one
invocation. Add a regression test where the existing test infrastructure can
exercise the behavior. A test should fail for the original defect and pass
with the fix; testing an unrelated helper is not equivalent.

Read the task output. `NO-SOURCE`, an empty test suite, or an up-to-date compile
task is not evidence that a gameplay bug has been exercised. If an automated
test is impractical, document a precise, repeatable manual scenario and its
observed result.

## Before opening the pull request

The current PR workflow assembles, runs tests, and checks both formatting and
Checkstyle. Run the corresponding repository-wide gate from the mod root:

```sh
./gradlew assemble test immaculateCheck checkstyle
```

`assemble` creates artifacts; it is not a substitute for tests or style checks.
Do not assume a generic `build` invocation or your IDE's compiler covers every
explicit gate above.

If you changed the API, also validate its documentation and generated reference:

```sh
./gradlew :api:javadoc :api:javamark
```

Inspect the result, not only the exit code. See
[API documentation](./api-documentation.md) for what must be documented.

## Exercise Minecraft behavior

Choose scenarios based on the change. Shared behavior needs attention on
**Fabric and NeoForge**; a loader-specific fix still needs verification that
the shared contract has not been broken.

The current development tasks include:

```sh
./gradlew :fabric:runClient
./gradlew :fabric:runServer
./gradlew :neoforge:runClient
./gradlew :neoforge:runServer
```

Run the relevant configuration separately and stop it normally when finished.
Use disposable worlds and accept Minecraft's EULA yourself where required.
Never use an irreplaceable world to test destructive or migration behavior.
Check the console and logs for errors, including errors that do not visibly
interrupt play.

| Change touches | Useful validation |
| --- | --- |
| Chiseling or placement | Survival and creative, tool breakage, insufficient bits, occupied space, inventory overflow, and undo/redo. |
| Selection or coordinates | Block faces and boundaries, negative coordinates, minimum/maximum build heights, and supported bit resolutions. |
| Multiplayer or side boundaries | Integrated client and dedicated server with a connected client; confirm server authority and no client-only classloading. |
| Variants, components, or codecs | Distinct material identities, encode/decode round trips, invalid input, saving/reloading, reconnecting, and full-block reconstruction. |
| Rendering or resources | World, item, and preview representations; resource reloads and affected visual states. |
| Permissions or automation | Allowed and denied areas, selections spanning claims, and operations without a player. |

The table is a starting point. Verify the actual requirement: if the fix is
about a count, assert the count; if it is about a rendered shape, inspect that
shape; if it is about persistence, reload the data.

## Validate website changes

From the **Website repository**:

```sh
npm ci
BASE=/Website npm run docs:build
```

`npm ci` installs the locked dependencies for a fresh checkout. For an existing
checkout with the correct dependencies, run the build directly.
`BASE=/Website` matches the current GitHub Pages workflow; use the workflow's
value if it changes. The assignment syntax above is for a POSIX shell.

Check the generated pages, links, sidebar order, code blocks, and production
base-path behavior. For interactive inspection:

```sh
BASE=/Website npm run docs:dev
```

A successful VitePress build validates Markdown/rendering and link processing,
**not Java snippets**. Compile substantial examples against the matching API
and check lifecycle/side assumptions against the implementation. Do not copy
an outdated API signature into a guide merely because the page renders.

## Handle failures honestly

Fix failures caused by your change. For an apparent pre-existing failure,
compare with the unmodified base using a separate checkout when needed, without
discarding someone else's work. Record the command, error, and evidence in the
pull request. Do not suppress a check, delete a test, swallow an exception, or
claim a pass when dependencies or the environment prevented execution.

After the final edit or formatter pass, rerun the affected checks. Results
from an earlier revision do not validate the final patch.

## Submission checklist

- The original issue is reproducible and the intended result is demonstrated.
- Relevant regression tests or repeatable manual checks cover the change.
- Assembly, tests, Immaculate, and Checkstyle pass, or blockers are explicitly reported.
- API changes include complete Javadoc and successful documentation generation.
- Directly affected guides, examples, translations, and resources are updated.
- The final diff contains no accidental formatting churn, debug code, secrets, or build artifacts.
- The pull request records commands, outcomes, tested environments, and any remaining limitations.
