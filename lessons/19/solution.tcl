proc mockFlow {design period} {
    if {$period <= 0} {error "Period must be positive"}
    return [list "read:$design" "clock:$period" "report:timing"]
}
puts [mockFlow Tiny 10]
