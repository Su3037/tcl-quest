namespace eval lab {
    proc area {w h} {return [expr {$w * $h}]}
}
puts [lab::area 6 7]
