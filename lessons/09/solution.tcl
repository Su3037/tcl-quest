proc clean {text} {
    return [string toupper [string trim $text]]
}
puts [clean "  chip  "]
