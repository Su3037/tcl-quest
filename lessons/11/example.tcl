proc greet {name {place Island}} {
    return "Hello $name at $place"
}
puts [greet Ada]
puts [greet Bo Forest]
