oo::class create Lamp {
    variable state
    constructor {} {set state off}
    method on {} {set state on}
    method status {} {return $state}
}
set lamp [Lamp new]
$lamp on
puts [$lamp status]
$lamp destroy
