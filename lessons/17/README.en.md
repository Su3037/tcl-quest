# 17 · Find a Clue in a Report

[中文](README.md) · [Course home](../../README.en.md)

A report line contains a slack value. Extract the number.

![Lesson 17 scene](../../site/media/scenes/level-17-en.svg)

regexp matches text against a regular-expression pattern. Parenthesized parts can capture a substring into a variable. A successful match returns 1; a failed match returns 0.

The pattern in this task allows an optional minus sign, integer digits and an optional decimal part. ^ and $ require the whole line to match. Return NA when the format does not match.

## Try this example

```tcl
set line "slack: -0.25"
if {[regexp {slack: (-?[0-9]+\.[0-9]+)} $line whole value]} {
    puts $value
}
```

## Your mission

Implement slackValue {line}. Accept the exact prefix slack: followed by an integer or decimal, optionally negative. Return the number text, or NA if it does not match. Print -0.25 for the sample.

Expected output:

```text
-0.25
```

## Hints

Use a capturing group for the number.

A suitable pattern is {^slack: (-?[0-9]+(\.[0-9]+)?)$}.

## Watch out

This is a simplified teaching format. Real tool reports require patterns based on that tool’s documented format and units.

## Think about it

What does negative slack mean in this teaching setting?

1. A timing requirement is not met
2. A file does not exist
3. The chip is already broken

<details><summary>Answer</summary>

A timing requirement is not met

</details>

## One more step

Try slack: 3, slack: -2.5 and a line without the slack prefix.
