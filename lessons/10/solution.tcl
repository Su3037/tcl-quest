proc supply {rows} {
    set selected {}
    foreach row $rows {
        lassign $row name hunger
        if {$hunger >= 5} {lappend selected $name}
    }
    return $selected
}
puts [supply {{Ada 7} {Bo 2} {Cy 5}}]
