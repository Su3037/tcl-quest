namespace eval lab {
    proc area {w h} {return [expr {$w * $h}]}
}
puts [lab::area 3 4]
