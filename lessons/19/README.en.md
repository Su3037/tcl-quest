# 19 · Build a Teaching Design Flow

[中文](README.md) · [Course home](../../README.en.md)

Separate configuration from operations so one script can serve different designs.

![Lesson 19 scene](../../site/media/scenes/level-19-en.svg)

source reads and executes another Tcl file in the current interpreter. Loading changeable parameters from a configuration file is a common way to organize scripts.

Real EDA read, constraint, synthesis, place-and-route and report commands vary between tools. mockFlow only returns a teaching description; it calls no commercial tool and produces no GDS.

## Try this example

```tcl
set f [open config.tcl w]
puts $f {set design Tiny}
close $f
source config.tcl
puts "Design: $design"
```

## Your mission

Implement mockFlow {design period}. Raise an error for period <=0; otherwise return the list {read:design clock:period report:timing}. Print the flow for Tiny with period 10.

Expected output:

```text
read:Tiny clock:10 report:timing
```

## Hints

Use if {$period <= 0} {error "Period must be positive"}.

Use list instead of string concatenation to preserve a design name containing spaces.

## Watch out

Here clock:10 is only text, not an EDA command that creates a real clock.

## Think about it

What does source config.tcl do?

1. Executes that Tcl file
2. Turns it into a video
3. Automatically starts commercial EDA software

<details><summary>Answer</summary>

Executes that Tcl file

</details>

## One more step

Try the design name My Chip and verify that llength still reports three steps.
