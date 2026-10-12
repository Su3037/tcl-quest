set rows {{p1 0.12} {p2 -0.25} {p3 -0.05}}
foreach row $rows {
    lassign $row path slack
    puts "$path -> $slack ns"
}
