# 06 · The Gatekeeper’s Choice

[中文](README.md) · [Course home](../../README.en.md)

The forest gate requires at least 10 coins. Help the gatekeeper make a choice.

![Lesson 6 scene](../../site/media/scenes/level-06-en.svg)

if means “if this condition holds”. A true condition runs one script; else supplies the alternative. Numeric comparisons include >=, < and ==.

For text comparisons, prefer eq and ne: if {$name eq "Ada"}. Tcl if conditions and branch scripts are usually enclosed in braces. A procedure scaffold is provided here; you will study procedures in more detail later.

## Try this example

```tcl
set coins 8
if {$coins >= 10} {
    puts "Enter"
} else {
    puts "Collect more"
}
```

## Your mission

Write gate {coins}. Return Enter for at least 10 coins and Wait otherwise. Print the result of gate 12.

Expected output:

```text
Enter
```

## Hints

Use if {$coins >= 10}.

Each branch should return its result: Enter or Wait.

## Watch out

The boundary value 10 must be allowed. Compare numbers with ==; assign values with set.

## Think about it

Which condition means “at least 10 coins”?

1. $coins >= 10
2. $coins > 10
3. $coins < 10

<details><summary>Answer</summary>

$coins >= 10

</details>

## One more step

Change the threshold to 20 and test 19, 20 and 21.
