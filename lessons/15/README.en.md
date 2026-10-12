# 15 · BOSS · Repair the Workshop

[中文](README.md) · [Course home](../../README.en.md)

The workshop needs an average skill card that also handles an empty basket.

![Lesson 15 scene](../../site/media/scenes/level-15-en.svg)

First add the values with foreach, then divide by the element count. An empty list has length 0; handle it before dividing.

Engineering scripts often calculate statistics. Use double to preserve fractional averages. The procedure accepts a single list argument, so group its values with braces at the call site.

## Try this example

```tcl
puts [llength {3 4 8}]
puts [expr {double(15) / 3}]
```

## Your mission

Implement average {numbers}. Return 0 for an empty list and the arithmetic mean otherwise. Print 5.0 for {2 4 9}.

Expected output:

```text
5.0
```

## Hints

Use llength to check for an empty list first.

After summing, return expr {double($total) / [llength $numbers]}.

## Watch out

incr works with integers. Using expr for this sum also supports decimal inputs.

## Think about it

Why use double in the average calculation?

1. To avoid losing fractions to integer division
2. To run the loop twice
3. To rename the variable

<details><summary>Answer</summary>

To avoid losing fractions to integer division

</details>

## One more step

Try {1.5 2.5} and verify the result is 2.0.
