set line "slack: -0.25"
if {[regexp {slack: (-?[0-9]+\.[0-9]+)} $line whole value]} {
    puts $value
}
