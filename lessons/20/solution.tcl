proc analyze {rows} {
    if {[llength $rows] == 0} {return [dict create violations 0 worst NA]}
    set violations 0
    set worst [lindex [lindex $rows 0] 1]
    foreach row $rows {
        lassign $row path slack
        if {$slack < 0} {incr violations}
        if {$slack < $worst} {set worst $slack}
    }
    return [dict create violations $violations worst $worst]
}
set result [analyze {{p1 0.12} {p2 -0.25} {p3 -0.05}}]
puts "Violations: [dict get $result violations]"
puts "Worst: [dict get $result worst] ns"
