proc supply {rows} {
    set selected {}
    foreach row $rows {
        lassign $row name hunger
        # 判断并添加名字
    }
    return $selected
}
puts [supply {{Ada 7} {Bo 2} {Cy 5}}]
