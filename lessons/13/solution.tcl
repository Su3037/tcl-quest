set f [open quest.txt w]
puts $f "Level 13"
puts $f "Saved"
close $f
set f [open quest.txt r]
puts [gets $f]
puts [gets $f]
close $f
