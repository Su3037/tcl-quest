# 20 · FINAL BOSS · Timing Report Detective

[中文](README.md) · [Course home](../../README.en.md)

Chip City’s timing report has arrived. Count violating paths and find the worst slack.

![Lesson 20 scene](../../site/media/scenes/level-20-en.svg)

The report is a list of {path slack} records. A slack below 0 counts as a violation; the smallest slack is the worst value. Return a dictionary so another script can use the results.

Handle empty input first. For nonempty input, initialize worst from the first actual record. Starting at 0 would incorrectly report 0 when all slack values are positive.

## Try this example

```tcl
set rows {{p1 0.12} {p2 -0.25} {p3 -0.05}}
foreach row $rows {
    lassign $row path slack
    puts "$path -> $slack ns"
}
```

## Your mission

Implement analyze {rows}, returning a dictionary with violations and worst. Empty input returns violations=0 and worst=NA. The sample prints Violations: 2 and Worst: -0.25 ns.

Expected output:

```text
Violations: 2
Worst: -0.25 ns
```

## Hints

Return early for empty input. Otherwise initialize worst from the first record.

In foreach, test slack<0 and slack<worst separately, then return a dict create result.

## Watch out

This is simplified teaching data. Real reports contain multiple checks and units; parse them according to the tool documentation.

## Think about it

If every slack is positive, what should worst contain?

1. The smallest positive value
2. Always 0
3. Always NA

<details><summary>Answer</summary>

The smallest positive value

</details>

## One more step

Extend the project: read records from a text file, skip blank lines, reject invalid data and write CSV.
