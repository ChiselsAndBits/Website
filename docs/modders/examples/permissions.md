---
title: Area permissions
order: 6
---

# Respect claims across the whole selection

A claim integration should check every Minecraft block touched by a chiseling
area, not just the block under the crosshair. This matters for drawn shapes,
large modes, and selections crossing a claim boundary.

`ClaimIntegration.java`:

```java
package com.example.cbcompat;

import java.util.Objects;
import java.util.UUID;
import java.util.function.BiPredicate;
import mod.chiselsandbits.api.permissions.ICheckerRegistration;
import mod.chiselsandbits.api.permissions.IPermissionHandler;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.LevelAccessor;

public final class ClaimIntegration implements AutoCloseable {
    @FunctionalInterface
    public interface ClaimQuery {
        boolean mayEdit(UUID player, LevelAccessor level, BlockPos pos);
    }

    private final ICheckerRegistration registration;

    public ClaimIntegration(
            ClaimQuery playerQuery,
            BiPredicate<LevelAccessor, BlockPos> automationQuery) {
        Objects.requireNonNull(playerQuery);
        Objects.requireNonNull(automationQuery);
        registration = IPermissionHandler.getInstance().registerChecker((player, area) ->
                area.coveredAreaStream().allMatch(pos -> player == null
                        ? automationQuery.test(area.getWorld(), pos)
                        : playerQuery.mayEdit(player.getUUID(), area.getWorld(), pos)));
    }

    @Override
    public void close() throws Exception {
        registration.close();
    }
}
```

Create and retain one instance when your claim integration becomes active.
The lambdas call **your claim mod's** dimension-aware lookup using the supplied
world and position. The second query handles edits without a player, such as a
machine. If your policy forbids all actorless edits, supply `(level, pos) -> false`.
Do not accidentally allow them because a player UUID is unavailable.

Close the instance when the integration or server-scoped claim service stops.
The returned token unregisters the checker; it is not a temporary result that
should be closed immediately after registration. `ICheckerRegistration` inherits
`AutoCloseable.close()`, so cleanup must handle its declared checked exception.

## How checks compose

All registered checkers must allow the edit. Returning `true` from your checker
does not override a denial from another protection mod.

C&B's chiseling context checks permissions when exposing its mutator. External
systems that use the raw mutator factory must explicitly call
`IPermissionHandler.getInstance().canManipulate(player, area)` before making
changes. Registering a checker is not a global interceptor for arbitrary world
modifications made by other code.

Keep the query fast and side-effect free: permission checks can run during
selection and preview, not just once on a server click. Do not load chunks,
perform network calls, or change claim state from the checker. If your claim
database is server-only, use its normal client-synchronized preview policy on
the client and enforce authoritative claims on the server.

## Verify denial and cleanup

Draw an area spanning an allowed and a denied claim: the entire operation should
be denied. Repeat with a selection fully inside the allowed claim and with an
actorless operation. Register a second checker that denies everything to confirm
your own allowance cannot override it. Finally, close the registration and verify
your checker no longer participates.
