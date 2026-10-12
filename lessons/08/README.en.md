# 08 · The Collecting Robot

[中文](README.md) · [Course home](../../README.en.md)

The robot can repeat a job without asking you to copy the same command many times.

![Lesson 8 scene](../../site/media/scenes/level-08-en.svg)

foreach takes each item from a list in turn and runs a script with that item. A running total starts at 0 and adds the current value on every turn.

for combines initialization, a condition and an update; while repeats while its condition is true. Make sure the condition can eventually become false. The task uses foreach.

## Try this example

```tcl
foreach fruit {apple pear} {puts $fruit}
for {set i 1} {$i <= 3} {incr i} {puts $i}
```

## Your mission

Visit 2, 4 and 6, accumulate their sum in total using foreach, and print 12.

Expected output:

```text
12
```

## Hints

Start with set total 0.

Inside foreach n {2 4 6}, use incr total $n.

## Watch out

Do not reset total inside the loop. That would discard the sum from previous turns.

## Think about it

What is easy to forget in a while loop?

1. Updating the state used by its condition
2. Writing PUTS in uppercase
3. Adding a website link

<details><summary>Answer</summary>

Updating the state used by its condition

</details>

## One more step

Try {1 3 5}, then an empty list. Predict each total.
