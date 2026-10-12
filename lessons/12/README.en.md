# 12 · Keep a Character Record

[中文](README.md) · [Course home](../../README.en.md)

Find an attribute by its name instead of remembering which numbered slot contains it.

![Lesson 12 scene](../../site/media/scenes/level-12-en.svg)

A dictionary stores key/value pairs, such as hp mapped to 80 and name mapped to Ada. dict get reads a value, dict set changes it and dict exists checks whether a key is present.

Tcl also has arrays: set hero(hp) 80. An array is a collection of variable elements; a dictionary is a value that can be passed as an argument. This task practices dictionaries.

## Try this example

```tcl
set hero [dict create name Ada hp 80]
dict incr hero hp 5
puts [dict get $hero hp]
set bag(key) 1
puts $bag(key)
```

## Your mission

Create a hero dictionary with name=Ada and hp=80. Increase hp by 20 and print Ada:100.

Expected output:

```text
Ada:100
```

## Hints

dict incr hero hp 20 updates the dictionary in variable hero.

dict get $hero hp reads the updated value.

## Watch out

Reading a missing key raises an error. You can check with dict exists first.

## Think about it

Which expression reads hp from the hero dictionary?

1. dict get $hero hp
2. set hero(hp)
3. lindex hp hero

<details><summary>Answer</summary>

dict get $hero hp

</details>

## One more step

Add a level key with the value 3.
