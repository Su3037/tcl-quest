# 14 · Avoid an Error Trap

[中文](README.md) · [Course home](../../README.en.md)

A locked chest should not end the whole adventure. Learn how to handle failure.

![Lesson 14 scene](../../site/media/scenes/level-14-en.svg)

catch runs a script and stores its result or error message in a variable. Completion code 0 means success; an ordinary error returns 1.

error reports an invalid situation explicitly. Errors are clues about your program. catch also handles completion codes such as return and break; this lesson concentrates on normal completion and ordinary errors.

## Try this example

```tcl
if {[catch {open missing.txt r} message]} {
    puts "Could not open file"
}
puts "Still running"
```

## Your mission

Implement safeDivide {a b}: return undefined when b is 0; otherwise use floating-point division. Print 2.5 for 5/2 and undefined for 5/0.

Expected output:

```text
2.5
undefined
```

## Hints

Check if {$b == 0} before dividing.

double($a) inside expr preserves fractions even with integer input.

## Watch out

Safe division can validate its input before an error occurs; it does not have to wait for division to fail.

## Think about it

What does a catch result of 0 usually mean?

1. The script completed normally
2. An ordinary error occurred
3. A file has size zero

<details><summary>Answer</summary>

The script completed normally

</details>

## One more step

Try catch {error "Bad key"} msg and then print $msg.
