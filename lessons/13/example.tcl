set f [open diary.txt w]
puts $f "Day 1: Ready"
close $f
set f [open diary.txt r]
puts [gets $f]
close $f
