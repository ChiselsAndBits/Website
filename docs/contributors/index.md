---
title: Contributor Documentation
order: 0
---

# Contributing to Chisels & Bits

Welcome! Contributions should leave the mod easier to maintain, preserve its
behavior on supported loaders, and include evidence that the change works.
A compiling patch alone is not a finished contribution.

| Before opening a pull request | Read |
| --- | --- |
| Follow the repository's formatting and static rules | [Code style and Immaculate](./code-style.md) |
| Reproduce the problem and validate the result | [Validating your work](./validation.md) |
| Document every API element and its contract | [API documentation](./api-documentation.md) |

## Get a development checkout

Fork and clone the
[mod repository](https://github.com/ChiselsAndBits/Chisels-and-Bits), then create a
focused branch from the version you intend to change. Check `gradle.properties`
for `java.version` and `minecraft.version`; the current development line uses
Java 25 and Minecraft 26.1.2. Other branches may differ.

Use the checked-in Gradle wrapper (`./gradlew`, or `gradlew.bat` on Windows),
not a separately installed Gradle version. Import the root Gradle project into
your IDE and let its configured plugins create the development environment.
The first build needs access to the configured dependency repositories.

## Put changes in the right place

| Location in the mod repository | Responsibility |
| --- | --- |
| `api/` | Contracts consumed by other mods. Every API element needs meaningful documentation. |
| `core/` | Shared mod implementation for the supported loaders. |
| `fabric/`, `neoforge/` | Loader-specific entrypoints, adapters, and integration. |
| `common/` | Shared build inputs, including the canonical code-style configuration. |

Prefer the existing shared implementation and Scena abstractions over duplicating
logic per loader. Keep client rendering dependencies behind the appropriate
physical-client boundary; an integrated client can hide dedicated-server
classloading failures.

This website lives in the separate
[Website repository](https://github.com/ChiselsAndBits/Website). Handwritten
guides belong there. Generated API reference pages originate from Javadoc in
the mod's `api/` sources; do not fix them only in the generated Markdown.

## Keep the patch reviewable

Solve one clearly described problem at a time. Follow nearby patterns, reuse
existing helpers, and avoid unrelated cleanup, dependency upgrades, or mass
formatting. Discuss substantial API or architecture changes with the maintainers
before investing in a large implementation.

Update the documentation, translations, resources, and tests directly affected
by the change. Preserve registry identifiers and serialized contracts unless
an intentional compatibility change includes a migration strategy. Explain
behavior changes rather than leaving reviewers to infer them from the diff.

## What belongs in the pull request

Describe the problem, reproduction steps, solution, and user-visible impact.
Link the relevant issue, explain compatibility considerations, and include
screenshots or recordings when visual behavior changes.

State the exact validation commands you ran and their results, along with
manual scenarios, loader, Minecraft version, and client/server environment.
Report skipped checks and blockers honestly. A successful CI run is useful
evidence, but does not replace checking the behavior you changed.

Before submitting, read your final diff, remove debugging and generated build
artifacts, and follow the [validation checklist](./validation.md#submission-checklist).