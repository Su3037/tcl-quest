proc average {numbers} {
    if {[llength $numbers] == 0} {return 0}
    set total 0
    foreach n $numbers {set total [expr {$total + $n}]}
    return [expr {double($total) / [llength $numbers]}]
}
puts [average {2 4 9}]
