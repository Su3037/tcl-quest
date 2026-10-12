set f [open config.tcl w]
puts $f {set design Tiny}
close $f
source config.tcl
puts "Design: $design"
