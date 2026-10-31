---
title: Plugin setup
order: 1
---

# Load a C&B integration

C&B discovers `IChiselsAndBitsPlugin` implementations using Java's `ServiceLoader`.
The annotation supplies optional filtering metadata; **the annotation alone does not
register a plugin**.

## Minimal plugin

`src/main/java/com/example/cbcompat/ExamplePlugin.java`:

```java
package com.example.cbcompat;

import mod.chiselsandbits.api.plugin.ChiselsAndBitsPlugin;
import mod.chiselsandbits.api.plugin.IChiselsAndBitsPlugin;

@ChiselsAndBitsPlugin(requiredMods = {"examplemod"})
public final class ExamplePlugin implements IChiselsAndBitsPlugin {
    @Override
    public String getId() {
        return "examplemod:cb_compat";
    }

    @Override
    public void onConstruction() {
        // Register common-side providers and deferred registrars here.
    }

    @Override
    public void onClientConstruction() {
        // Call a separate client-only integration class here.
    }

    @Override
    public void onInitialize() {
        // Resolve registered entries here, if your integration needs them.
    }
}
```

Create the service file
`META-INF/services/mod.chiselsandbits.api.plugin.IChiselsAndBitsPlugin`:

```text
com.example.cbcompat.ExamplePlugin
```

The class must be public and have a public no-argument constructor (the implicit
constructor above is sufficient). Preserve the service file when assembling or
shading your JAR. Merge service entries if several integrations share an artifact.

## Choose the right callback

| Callback | Typical work |
| --- | --- |
| `onConstruction()` | Register variant providers with lazy block suppliers; initialize a Scena deferred registrar for custom modes. |
| `onClientConstruction()` | Register client variant providers. Keep renderer/model classes out of common-side fields and static initializers. |
| `onInitialize()` | Work requiring completed Minecraft registrations, rather than declaring new registry entries. |

C&B installs its API instance and declares its built-in registries before invoking
plugin construction. Do not query API managers in your mod's unrelated early static
initializers, and do not resolve deferred blocks or modes while declaring them.
Keep plugin constructors free of registration side effects.

The API permits callbacks to run alongside other initialization work. Avoid shared
mutable setup state and do not assume another plugin has run first.

## Dependencies and optional integration

Follow [Gradle setup](../gradle-setup.md) for repositories, exact artifact
coordinates, and loader-specific development runtime dependencies.

Compile against the matching published API (`mod.chiselsandbits:api`)
and the matching Minecraft/loader development dependencies. The API exposes Scena
types, so do not strip its transitive dependencies from your compile classpath.
Install the matching full C&B mod and its required dependencies for development
runs; the API library alone is not a runtime implementation.

Use the same version as your installed C&B build; do not mix a current API
with an older runtime.

If C&B is optional, keep these classes behind your loader's optional-integration
boundary. Do not reference C&B types from eagerly loaded mod entrypoints when C&B
is absent. `requiredMods` filters plugins discovered **by C&B**; it is not a general
classloading guard for your own code. Your mod's loader metadata must also express
the appropriate dependency and load ordering.

## Add the examples

The following guides show replacement bodies for these callbacks. Combine them in
one plugin, rather than registering the same provider or registrar more than once.

Use the **same provider identifiers and mode identifiers on client and server**.
They are serialized identities, not display names. Renaming or removing them can
make existing saved data or item components unreadable.

## Check discovery

Build your mod JAR and inspect it:

```sh
jar tf build/libs/your-mod.jar
```

Confirm that the service file and implementation class are present. At startup,
C&B logs plugin discovery and each callback with the plugin ID. If an integration
is missing, check the service file, required mod IDs, dependency versions, and
classloading errors before debugging the provider itself.
