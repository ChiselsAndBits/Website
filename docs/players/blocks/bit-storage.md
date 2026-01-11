---
layout: doc
title: Bit Storage
order: 2
summary:
    icon: https://raw.githubusercontent.com/ChiselsAndBits/Assets/refs/heads/main/Icons/InGame/chiselsandbits/bit_storage.png
    summary: Bit storage, your gateway in storing and automating bits
    title: Bit Storage
    recipe:
      ingredients:
        "c":
          namespace: chiselsandbits
          location: chisel
          isTag: true
        "g":
          namespace: c
          location: glass_blocks
          isTag: true
        "i":
          namespace: c
          location: ingots/iron
          isTag: true
        "l":
          namespace: minecraft
          location: logs
          isTag: true
      contents:  [
        "igi",
        "glg",
        "ici"
      ]
---

# Bit Storage
The bit storage allows you to store bits of a block or fluid inside it. As well as automatically replenish itself when it runs out through automations
using a hopper or dispenser.

### Possible interactions
The Bit Storage has no interface, but you can interact with it by `Right`-clicking it while holding different items, or even nothing.

#### `Right`-Clicking with a bit
When you perform this interaction, there are two possible situation that might apply. When there are already bits in the inventory you have to hold `Shift` (crouch), which 
will insert the held stack into the storage if the bits match the ones already in the storage.
If the storage is empty then it will insert the bits regardless of whether you are holding shift (are crouching) or not.

#### `Shift`+`Right`-Clicking with an empty hand
When you perform this interaction, the storage will extract as many bits of the already stored bit as it can from your inventory. Possibly extracting from other bit inventories (like bit bags).
If the storage is empty, nothing happens.

#### `Right`-Clicking in other situations
If you `Right`-click with a tool, or an insertion is not possible, then the storage assumes you want to extract a stack of bits from the storage. If it has that much to give it will happily insert them into your inventory, unless that inventory is full. In that case it will drop them.

> [!NOTE]
> This works perfectly when combined with bit bags and their pickup priority modes. The bit storage will respect these.

---

### Chaining storages
As a single bit storage can only store the bits of a single block, it might be a bit limiting when it comes to using it in automations, or when building large structures.
As such you can stack several storages on top of each other, and they will act as a single larger bit storage, with virtual hoppers in between them. Automatically drawing from storage directly above them and pushing the bits down below, as long as they are of the same bits type.
To increase the storage even further you can stick a real hopper on top of the highest bit storage and it will automatically insert a block into it. 
Or use a dispenser with comparators and redstone to trigger a dispensing of a supported fluid into the storage when it runs out. 
