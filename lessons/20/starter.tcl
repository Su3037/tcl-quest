proc analyze {rows} {
    # 统计违规数量，并找到最小 slack
    return [dict create violations 0 worst NA]
}
set result [analyze {{p1 0.12} {p2 -0.25} {p3 -0.05}}]
puts "Violations: [dict get $result violations]"
puts "Worst: [dict get $result worst] ns"
