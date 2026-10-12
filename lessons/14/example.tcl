if {[catch {open missing.txt r} message]} {
    puts "Could not open file"
}
puts "Still running"
