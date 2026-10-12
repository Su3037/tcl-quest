oo::class create Chip {
    variable name
    constructor {value} {set name $value}
    method label {} {return "TODO"}
}
set chip [Chip new Tiny]
puts [$chip label]
$chip destroy
