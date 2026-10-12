proc slackValue {line} {
    if {[regexp {^slack: (-?[0-9]+(\.[0-9]+)?)$} $line whole value]} {return $value}
    return NA
}
puts [slackValue "slack: -0.25"]
