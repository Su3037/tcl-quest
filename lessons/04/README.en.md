# 04 · Brew an Energy Potion

[中文](README.md) · [Course home](../../README.en.md)

Let Tcl calculate the energy in your potion recipe.

![Lesson 4 scene](../../site/media/scenes/level-04-en.svg)

expr evaluates arithmetic. set energy [expr {3 * 7}] calculates 21 and stores it. Braces around the expression let expr handle its variables safely and efficiently.

incr energy 4 adds 4 to an integer variable. Integer division drops the fractional part: 5 / 2 is 2, while 5 / 2.0 is 2.5.

## Try this example

```tcl
set base 6
set power [expr {$base * 3}]
incr power 2
puts $power
puts [expr {5 / 2.0}]
```

## Your mission

There are 3 bottles with 7 energy each and a bonus of 4. Store the total in energy and print 25.

Expected output:

```text
25
```

## Hints

Multiply the bottle count by the energy per bottle using expr.

Then use incr energy 4 and puts $energy.

## Watch out

incr expects an integer increment. Use expr when your calculation needs fractions.

## Think about it

What is the result of expr {5 / 2}?

1. 2
2. 2.5
3. An error

<details><summary>Answer</summary>

2

</details>

## One more step

Try a different bottle count and calculate the expected total yourself.
