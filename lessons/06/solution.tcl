proc gate {coins} {
    if {$coins >= 10} {return Enter} else {return Wait}
}
puts [gate 12]
