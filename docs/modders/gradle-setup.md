---
title: Gradle setup
order: 1
---

# Consume the API from Gradle

Compile your integration against the **API artifact**, and run it with the
**full mod for your loader**. The API JAR contains contracts, not the working
implementation of `IChiselsAndBitsAPI`.

These snippets extend an existing Minecraft mod development project. They do
not replace your loader plugin, Minecraft dependencies, run configurations,
or mod metadata. Examples use Groovy DSL (`build.gradle`) and target
**Minecraft 26.1.2 / Java 25**.

## Coordinates and versions

| Purpose | Maven coordinate |
| --- | --- |
| Compile-time API | `mod.chiselsandbits:api:<version>` |
| Fabric development runtime | `mod.chiselsandbits:fabric:<version>` |
| NeoForge development runtime | `mod.chiselsandbits:neoforge:<version>` |

These are Maven artifact IDs, not the longer names of downloaded distribution
JARs. Do not use `chisels-and-bits-api` as the artifact ID for this version line.
The loader mod ID is `chiselsandbits`.

Pin a published C&B version for the Minecraft version you target, and use that
**same version** for the API and runtime. For example, `26.1.2.71` is a published
version used below. It is an example pin, not a promise that it is the latest
release or compatible with other Minecraft versions.

In `gradle.properties`:

```properties
chiselsandbits_version=26.1.2.71
```

Do not copy the repository's `*-local-*` development version into a remote
dependency declaration; it is not necessarily published. Avoid `+` for the
C&B version so a new release cannot silently change your integration's target.

## Add dependency repositories

Add these to the **dependency** repositories in `build.gradle`, alongside your
loader's normal repositories:

```groovy
repositories {
    mavenCentral()
    maven {
        name = 'ChiselsAndBits'
        url = uri('https://ldtteam.jfrog.io/artifactory/chisels-and-bits-chisels-and-bits')
        content {
            includeGroup 'mod.chiselsandbits'
        }
    }
    maven {
        name = 'Scena'
        url = uri('https://ldtteam.jfrog.io/artifactory/communi-suggestu-maven')
        content {
            includeGroup 'com.communi-suggestu.scena'
            includeGroup 'com.communi-suggestu.saecularia-caudices'
        }
    }
}
```

The API exposes Scena types and declares Scena's common library transitively.
The second repository is therefore required even if your own source imports
only C&B types. Its content filter also allows Saecularia Caudices, a transitive
Scena dependency. Do not disable transitive resolution on the API dependency.
Maven Central supplies ordinary supporting libraries.

If your build centralizes repositories with
`dependencyResolutionManagement.repositories` in `settings.gradle`, put the
repositories there instead. Adding them only to `pluginManagement.repositories`
will not make normal library dependencies resolvable.

## Compile against the API

In the module containing your integration:

```groovy
def cbVersion = providers.gradleProperty('chiselsandbits_version').get()

dependencies {
    compileOnly "mod.chiselsandbits:api:${cbVersion}"
}
```

`compileOnly` makes the API available to your Java compiler without making
your mod responsible for shipping a second copy of it. Keep implementation
imports inside `mod.chiselsandbits.api`; depending on C&B's internal `core`
classes makes the integration fragile.

Do not use Gradle's `api` or `implementation` configurations merely because
the artifact is called `api`. Those configurations express dependency exposure
and classpath semantics, not the kind of library being consumed. For a normal
mod integration, `compileOnly` is the appropriate compile-time boundary.

## Add the loader runtime for development

Choose **one** of the following blocks in the appropriate loader module. Keep
the `cbVersion` declaration and API dependency from the previous section.

### Fabric on Minecraft 26.1+

For an existing unobfuscated Fabric Loom project:

```groovy
dependencies {
    runtimeOnly("mod.chiselsandbits:fabric:${cbVersion}") {
        transitive = false
    }
}
```

Minecraft 26.1+ uses unobfuscated names. Modern
`net.fabricmc.fabric-loom` projects use standard `compileOnly` and `runtimeOnly`
configurations, not the old `modCompileOnly` / `modRuntimeOnly` remapping
configurations. See Fabric's
[26.1 tooling guidance](https://fabricmc.net/2026/03/14/261.html).

Keep Fabric Loader and Fabric API configured by your normal Fabric development
template, at versions supported by the selected C&B release. The runtime block
above deliberately does not choose or upgrade them for you.

### NeoForge

For an existing NeoForge development project whose runs use the main source
set's runtime classpath:

```groovy
dependencies {
    runtimeOnly("mod.chiselsandbits:neoforge:${cbVersion}") {
        transitive = false
    }
}
```

Keep your normal NeoForge plugin and Minecraft/NeoForge version configuration.
If you use custom run source sets or a development-only runtime configuration,
attach this dependency to the configuration those runs actually consume.
An entry on an unrelated project's runtime classpath does not install a mod
in your game's run configuration.

### Why disable runtime transitives?

For the release shown here, the full Fabric and NeoForge artifacts already
contain the API, shared C&B implementation, and loader-specific Scena library
as nested JARs. Their Maven metadata also describes dependencies on C&B
modules and development tooling. Resolving that entire graph separately can
introduce unnecessary artifacts or duplicate copies of bundled libraries.

The runtime blocks therefore select the **complete loader JAR** without its
Maven transitive graph. This is separate from the API compile dependency,
whose transitives remain enabled. Do not add a standalone API or common
`core` JAR as another runtime mod.

This assumes the selected runtime release retains that packaging. If you
target another version line, inspect its artifact and declared loader
requirements rather than applying these exclusions blindly. External loader
requirements, notably Fabric API, still need to be installed/configured.

::: warning Do not redistribute C&B inside your integration
Do not shade C&B classes or use Loom `include`, NeoForge `jarJar`, or a fat-JAR
task to embed the API or full mod into your own distribution. Your integration
consumes the installed C&B mod; it does not supply a replacement API singleton
or another C&B implementation.
:::

## Multi-loader projects

Declare `compileOnly "mod.chiselsandbits:api:${cbVersion}"` in the common module
that compiles shared integration code. Put only the matching runtime artifact
in each platform module: Fabric in Fabric, NeoForge in NeoForge.

Gradle's `compileOnly` dependencies are not automatically exported to consumers.
If a loader module also compiles source that directly references C&B/Scena
types, give that module the API compile dependency as well. Keep one version
property at the root and follow your build's existing shared-source wiring.

Do not put both full loader artifacts on a common runtime classpath. The API
artifact is loader-neutral, but it still needs a matching Minecraft development
classpath; a plain Java project without Minecraft classes is not sufficient
to compile an integration.

## Declare the runtime relationship in mod metadata

Gradle dependencies configure **your development build**. They do not tell a
player's mod loader or a distribution platform to install C&B.

Declare `chiselsandbits` in your loader metadata with an appropriate supported
version range and dependency ordering. If the integration is required, make
C&B required. If it is optional, use the loader's optional dependency mechanism
and isolate all C&B references behind an optional-integration boundary.
Update distribution-platform dependency declarations too, where applicable.

A `compileOnly` declaration alone does not make an integration safe when C&B
is missing. In particular, do not access API managers from eager static
initializers. C&B's `@ChiselsAndBitsPlugin(requiredMods = ...)` filters plugins
when C&B discovers them; it does not protect unrelated code that your own mod
loads first.

Continue with [plugin setup](./examples/plugin-setup.md) for the service file
and registration callbacks.

## Verify the dependency setup

From your mod's project, inspect both classpaths:

```sh
./gradlew dependencyInsight --dependency mod.chiselsandbits --configuration compileClasspath
./gradlew dependencyInsight --dependency mod.chiselsandbits --configuration runtimeClasspath
./gradlew compileJava
```

Prefix the tasks with your module path in a multi-project build. The compile
classpath should contain the API and its Scena compile dependency. The runtime
classpath should contain the full mod for your loader; the API is supplied at
game runtime by that mod's bundled libraries.

Launch your normal client and dedicated-server development runs. Confirm that
C&B and your plugin load, check the selected versions, and exercise an actual
API call after initialization. For optional integrations, also test a run
without C&B; temporarily remove the development runtime dependency for that
separate check.

| Symptom | Check |
| --- | --- |
| Artifact not found | Use `mod.chiselsandbits:api`, a published version, and the dependency repositories above. |
| Scena types are missing | Retain API transitives and the Scena repository; ensure your loader source set also has the API compile dependency if needed. |
| Incompatible JVM variant / class-file version | Run Gradle and the Java toolchain with the Java version required by that C&B/Minecraft line (25 here). |
| API compiles but managers are unavailable at runtime | Install the full matching loader mod and access the API at a valid initialization phase. |
| Duplicate classes or mods | Remove separately installed API/core libraries, accidental shading, and duplicate runtime copies; inspect nested-JAR packaging. |
| Works in the IDE but not a packaged mod | Check loader metadata, runtime installation, service-file packaging, and optional classloading boundaries. |
