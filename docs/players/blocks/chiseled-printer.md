---
title: Chisel Station
order: 3
summary:
  icon: https://raw.githubusercontent.com/ChiselsAndBits/Assets/refs/heads/main/Icons/InGame/chiselsandbits/chiseled_printer.png
  summary: The chisel station, also called the printer, allows for rapid duplication of chiseled blocks.
  recipe:
    ingredients:
      "l":
        namespace: minecraft
        location: logs
        isTag: true
      "c":
        namespace: chiselsandbits
        location: chisel
        isTag: true
      "s":
        namespace: minecraft
        location: smooth_stone_slab
        isTag: false
        title: Smooth stone slab
    contents:  [
      " c ",
      "l l",
      "sss"
    ]
---
# Chisel Station
The chisel station, also called the printer, allows for rapid duplication of chiseled blocks.
By placing it surrounded by the required bit storages it will draw the bits from the pattern it holds to create copies of the block
inside it.

This block has not much use in creative play, as a simple `Middle`-click (while sneaking) will copy any chiseled block into your creative inventory,
but in survival play it is extremely useful as it can make many thousands of duplicates while you work on other things.

## Source of bits
The chisel station needs a source of bits so that it can create the duplicates.
It will look for bit storages attached to either of the three sides horizontally which are not the front (so the back, left and right sides of the station, the front side is the side with the buttons).
It will consider any storage attached directly to it, or to any already recognized storage in that direction, for up to 16 blocks. It won't make any turns while looking, and any none bit storage will make it stop looking in that direction.

Two stations can share a row of bit storages when they are placed on either end from the chain of storages, and will happily share them while creating duplicates.

A station needs all the bits from the source pattern present in the storages it considers valid before it starts producing a duplicate.

## Interface
`Right`-Clicking the block opens up its interface:
<div style="justify-content: center !important; display: flex;">
    <img style="" src="https://raw.githubusercontent.com/ChiselsAndBits/Assets/refs/heads/main/Interfaces/chiseled_printer.png" width=300 alt="Chisel station interface">
</div>

This interface is made up out of 2 sections.
The lower section is your inventory, you can use it to pick the patterns you want to duplicate, as well as the chisel needed as a tool, or store the resulting output after the duplicate has been created.

The upper section is made up out of three slots, and a progress indicator.
The left slot is the pattern input (it does not matter whether the pattern is sealed or not).
The top slot needs to contain a valid chisel, each duplication damages the chisel by one action.
The right slot is the output slot.

In the middle, between all three slots, you will find the progress indicator, which will increasingly render a colored chisel while the bits are collected and printed.

> [!TIP]
> The pattern is not damaged by this machine. So use an unsealed pattern if you want!

