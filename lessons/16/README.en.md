# 16 · Enter Chip City

[中文](README.md) · [Course home](../../README.en.md)

Take your everyday automation skills into a chip-design setting.

![Lesson 16 scene](../../site/media/scenes/level-16-en.svg)

VLSI means very-large-scale integration; EDA software helps people design chips. Tcl often controls these tools, but the additional tool commands are not built into Tcl itself.

A namespace groups related commands and helps avoid name conflicts. Our lab::area is a teaching command that calculates a rectangle’s area; it does not perform real chip design.

## Try this example

```tcl
namespace eval lab {
    proc area {w h} {return [expr {$w * $h}]}
}
puts [lab::area 3 4]
```

## Your mission

Inside namespace lab, implement area {w h} to return width times height. Print 42 for lab::area 6 7.

Expected output:

```text
42
```

## Hints

Define proc area inside namespace eval lab {...}.

Return [expr {$w * $h}].

## Watch out

EDA commands depend on the specific tool. They may not exist in an ordinary Tcl interpreter.

## Think about it

Is create_clock a built-in Tcl core command?

1. No; it is usually provided by an EDA tool
2. Yes; every tclsh can run it
3. It is a browser command

<details><summary>Answer</summary>

No; it is usually provided by an EDA tool

</details>

## One more step

Create another namespace with its own area command and compare the full names.
