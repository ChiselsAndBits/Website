---
title: API documentation
order: 3
---

# Document the entire API contract

**Every element of the `api` module needs meaningful documentation.** Treat
documentation as part of implementing an API, not as optional follow-up work.
Another mod author should be able to use an element correctly without reading
C&B's internal implementation.

## What must be covered

Document packages (`package-info.java`), classes, interfaces, records, enums,
annotations, constructors, methods, constants, fields, enum values, record
components, and annotation members. Include nested types and generic type
parameters. An implicit constructor or generated accessor is not a reason to
leave the exposed contract unexplained; cover the relevant behavior in its
type, record-component, or constructor documentation.

For overridden methods, inherit an adequate contract where appropriate, but
document any additional guarantees, restrictions, or behavior. Do not paste a
second copy of an inherited description that will drift out of date.

Javadoc tooling checks only the elements and diagnostics within its configured
scope. A successful generation task is necessary, but it does not prove that
every API element is documented well. Review completeness yourself, including
elements not flagged by doclint.

## Explain behavior, not just names

Each API description should answer the questions relevant to that element:

| Contract detail | What to explain |
| --- | --- |
| Purpose | What the element represents and when an integrator should use it. |
| Inputs and outputs | Units, coordinate space, valid ranges, collection contents, optional/empty cases, and nullability. |
| Ownership | Whether values are mutable, immutable, copied, live views, or snapshots; whether callers may retain or modify them. |
| Lifecycle | Registration timing, lazy suppliers, valid initialization phases, and required cleanup. |
| Execution | Logical side, physical-client restrictions, owning-thread requirements, and possible parallel callbacks. |
| Effects and failure | World or inventory changes, simulation semantics, error reporting, and documented exceptions. |
| Compatibility | Registry identities, serialization formats/codecs, persistence expectations, and migration implications. |

Be precise where the API is easy to misuse. Distinguish local block coordinates
from world coordinates, a bit count from a block count, an empty result from an
error, and a detached snapshot from an immutable object.

Use `@param` for value and type parameters, `@return` (or an appropriate inline
`{@return ...}`) for results, and `@throws` for relevant failure conditions.
Keep tags in the repository's configured order. Explain constructor parameters
and record components as carefully as method parameters.

Use `{@link ...}` for related types and methods and `{@code ...}` for identifiers
and literal values. Escape special characters correctly; malformed Javadoc
can break both HTML documentation and the website's generated reference.
Add `@implNote` only for useful implementation context, without presenting
an incidental implementation detail as a permanent API guarantee.

## Example: useful value-type documentation

This illustrative API declaration documents both the purpose and the input
contract. It is not a request to add a new RGB type to C&B:

```java
/**
 * Immutable RGB value used to distinguish decorative material colors.
 *
 * <p>The value contains no alpha channel and does not retain a world or block entity.
 *
 * @param rgb color packed as {@code 0xRRGGBB}, from {@code 0x000000} to {@code 0xFFFFFF}
 */
public record MaterialColor(int rgb) {
	/**
	 * Creates a decorative material color.
	 *
	 * @param rgb packed 24-bit RGB color
	 * @throws IllegalArgumentException if the value is outside the 24-bit RGB range
	 */
	public MaterialColor {
		if (rgb < 0 || rgb > 0xFFFFFF) {
			throw new IllegalArgumentException("Expected 24-bit RGB");
		}
	}
}
```

Avoid descriptions such as "Gets the value" or "The parameter" when the important
information is what that value means, which units it uses, or who owns it.
Do not promise immutability, automatic permission enforcement, or thread safety
unless the implementation actually provides it.

## Strict Javadoc validation

The API build explicitly enables missing-documentation doclint
(`Xdoclint:missing`) and treats Javadoc warnings as errors (`Werror`).
Other implementation/documentation modules currently mute missing-comment
diagnostics; **that exception does not apply to `api`**.

From the mod repository:

```sh
./gradlew :api:javadoc :api:javamark
```

Review the HTML under `api/build/docs/javadoc` and the Markdown under
`api/build/docs/markdown`. Check links, signatures, type parameters, paragraphs,
and descriptions in the generated output. Fix warnings and malformed references
in source; do not turn off doclint or warning-as-error settings.

Checkstyle also checks Javadoc style and tag order. It does not replace the
strict generation step or a human review of accuracy.

## Source documentation and website examples

The publishing workflow exports `:api:javamark` output into the Website
repository's `docs/modders/api`. That directory is generated reference material.
Fix source Javadoc in the mod repository so the next export preserves the fix.
Do not commit build output in the mod repository as a substitute.

When a contract changes, update the affected
[modder examples](../modders/examples/index.md) and other handwritten guides too.
Reference documentation should explain the contract; examples should demonstrate
a realistic, correct use of it, including registration, side boundaries,
serialization, and failure handling when relevant.

## Compatibility is part of documentation

An API change can affect mods that are not in this checkout. Review source and
binary compatibility, implemented interfaces, defaults, serialized identifiers,
and data formats. Explain intentional breaking changes and their migration
path in the pull request and user-facing documentation as appropriate.

Keep the documented contract and implementation in the same patch. A new
parameter, changed return meaning, or altered threading requirement is not
complete until callers can discover the new behavior from the API itself.
