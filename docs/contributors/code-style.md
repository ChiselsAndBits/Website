---
title: Code style and Immaculate
order: 1
---

# Code style and Immaculate

The source of truth is
[`common/codestyle/checkstyle.xml`](https://github.com/ChiselsAndBits/Chisels-and-Bits/blob/HEAD/common/codestyle/checkstyle.xml)
in the mod repository. Use the file from **your checked-out branch**, not an
IDE's default Java style or a copied configuration from another project.

## How the tools fit together

**Checkstyle verifies the rules. Immaculate applies and checks formatting.**
The two tools are complementary, not alternatives.

The root `build.gradle` applies Checkstyle across projects and points it at
the shared XML. The current Checkstyle version is 10.21.4. The `checkstyle`
task includes both `checkstyleMain` and `checkstyleTest`.

The shared
`common/conventions/chiselsandbits.settings.codestyle-conventions.gradle`
registers Immaculate's Java workflow through Formatum/Adhibe. Its Checkstyle
step uses the same XML plus
`common/codestyle/checkstyle-immaculate-hints.yaml`, with aggressive fixes and
`failOnUnmatchedHints = true`. The conventions are applied through
`settings.gradle`.

Do not edit these files to accommodate an ordinary patch. A style-policy change
is a separate, deliberate change that must keep Checkstyle and Immaculate in sync.

## Format, inspect, then verify

Run commands from the **mod repository**, not this website:

```sh
./gradlew :core:immaculateApply
git diff --stat
git diff
./gradlew :core:immaculateCheck :core:checkstyle
```

Replace `:core` with the module you changed. For the complete repository:

```sh
./gradlew immaculateCheck checkstyle
```

`immaculateApply` **modifies files**. Its Java apply task is configured to run
even when Gradle would otherwise consider it up to date. Start with a known
working-tree state, scope it to the relevant modules, and review every resulting
change. Aggressive fixes are not proof that the resulting code still means
the same thing.

Some checks intentionally have no automatic rewrite. Fix those violations in
the source; do not weaken the rule, disable unmatched-hint failures, or add a
blanket suppression just to get a green build. Run both verification tasks
after formatting, and repeat the relevant behavioral validation after any
semantic change.

## Rules to know before writing code

This is a guide to frequently encountered rules, not a replacement for the XML.

| Area | Repository convention |
| --- | --- |
| Indentation | Tabs, with a Checkstyle tab width of four; continuation indentation is eight columns and `case` labels have no extra case indent. |
| Whitespace | No trailing whitespace, a newline at EOF, no repeated blank lines or blank padding immediately inside braces. Follow the configured blank-line separation around blocks. |
| Imports | Explicit imports; no wildcard, unused, or redundant imports. Groups are `java`, `javax`, other libraries, `net.minecraft`, then `net.fabricmc`, with separation and configured ordering. Static imports are ordered at the top. |
| Braces | Opening braces at the end of the line. Follow `NeedBraces`; do not introduce ambiguous unbraced control flow. |
| Types | `var` is allowed only for a local initialized with a direct `new` expression; use an explicit type for method results and other expressions. |
| Nullability | Use `org.jspecify.annotations.Nullable`, not JetBrains `Nullable`. `@NotNull` is prohibited by the current rules. Respect the package's nullability contract. |
| Assertions and debugging | Java `assert` statements and `@Debug` annotations are prohibited. Use the test framework's assertions in tests and explicit validation/errors in production code. |
| Structure | Follow modifier order, add required `@Override` annotations, and avoid excessive nesting; the configuration rejects blocks nested beyond six levels. |
| Javadoc | Follow Javadoc style/paragraph checks and tag ordering: `@param`, `@return`, `@throws`, `@deprecated`. API completeness is additionally enforced by Javadoc generation. |

Prefer clear names and simple control flow. Explain non-obvious intent in a
short comment rather than narrating each statement. Localize user-facing text
using the existing translation conventions.

The checker permits some explicitly marked ignored exceptions; that is not
permission to hide errors. Follow the existing error-reporting contract and
preserve diagnostics when an operation cannot complete.

## Mixin-specific checks

Mixin fields must have `@Unique` or `@Shadow`. Methods must have `@Unique` or
one of the explicitly allowed Mixin/MixinExtras annotations in the XML.

Use MixinExtras `@Local` rather than `@Inject(locals = ...)` capture.
The current rules prohibit `ordinal` on parameter `@Local` annotations and
prohibit combining `name` with `argsOnly` on the same annotation.
If an injection changes, verify the target and behavior on the relevant loader;
passing Checkstyle does not establish that an injection still applies.

## Configure your IDE without replacing the build checks

Point your Checkstyle integration at the repository XML and use a compatible
Checkstyle version. Configure tabs and import handling accordingly, or let
Immaculate perform the final formatting pass.

IDE inspections and formatter previews are feedback, not the acceptance
criterion. The Gradle tasks use the repository's actual configuration.
Do not commit personal IDE paths, local caches, or editor-only formatting
changes as part of an unrelated fix.
