proc safeDivide {a b} {
    if {$b == 0} {return undefined}
    return [expr {double($a) / $b}]
}
puts [safeDivide 5 2]
puts [safeDivide 5 0]
