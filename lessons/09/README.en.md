# 09 · Transform a Sign

[中文](README.md) · [Course home](../../README.en.md)

Clean a messy sign, convert the letters and hang up the new version.

![Lesson 9 scene](../../site/media/scenes/level-09-en.svg)

string trim removes whitespace at the beginning and end of text. string toupper converts letters to uppercase. You can nest bracketed commands so that one result becomes another command’s input.

split turns text into a list using separator characters. join combines list elements with a chosen separator. They are useful for moving between structured data and readable text.

## Try this example

```tcl
set raw "  chip island  "
puts [string toupper [string trim $raw]]
puts [join {A B C} "-"]
```

## Your mission

Write clean {text} to trim both ends and convert to uppercase. Print the result for "  chip  ": CHIP.

Expected output:

```text
CHIP
```

## Hints

Apply string trim to $text first.

Return [string toupper [string trim $text]].

## Watch out

trim does not remove spaces in the middle of the text. Preserve those when cleaning a multiword sign.

## Think about it

Which command removes spaces at both ends of a string?

1. string trim
2. string length
3. llength

<details><summary>Answer</summary>

string trim

</details>

## One more step

Try "  chip island  " and check that the middle space remains.
