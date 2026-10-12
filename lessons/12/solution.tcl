set hero [dict create name Ada hp 80]
dict incr hero hp 20
puts "[dict get $hero name]:[dict get $hero hp]"
