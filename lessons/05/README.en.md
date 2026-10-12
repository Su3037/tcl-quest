# 05 · BOSS · Repair the Launch Beacon

[中文](README.md) · [Course home](../../README.en.md)

The launch beacon needs its name, energy and original template restored.

![Lesson 5 scene](../../site/media/scenes/level-05-en.svg)

Combine the skills from the village: store values with set, calculate with expr and display with puts. Think about whether each output should contain a value or literal text.

Double quotes replace variables; braces preserve the literal template in this task. These three output lines deliberately use different rules.

## Try this example

```tcl
set name Beacon
set power [expr {4 * 5}]
puts "$name: $power"
```

## Your mission

Set hero=Ada, cells=4 and each=5. Store their product in energy. Print Ada ready, Energy: 20, and the literal text $energy on three lines.

Expected output:

```text
Ada ready
Energy: 20
$energy
```

## Hints

Use expr {$cells * $each} for the energy.

Use braces around $energy on the final output line.

## Watch out

The last line must preserve $energy; printing 20 again does not satisfy this part of the task.

## Think about it

Which approach makes a bug easier to find?

1. Change one thing and run it
2. Change every line at once
3. Delete all the brackets

<details><summary>Answer</summary>

Change one thing and run it

</details>

## One more step

Change the hero and battery count and predict which output lines will change.
