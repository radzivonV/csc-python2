def print_map(m, pos):
    visual_m = [['.' if col else '#' for col in row] for row in m]
    visual_m[pos[0]][pos[1]] = '@'
    string_m = '\n'.join([''.join(row) for row in visual_m])
    print(string_m)


def shape(m):
    assert m, "map must be not empty"
    return len(m), len(m[0])


def neighbours(m, pos):
    nrows, ncols = shape(m)
    ns = []
    if any([pos[0] >= nrows, pos[1] >= ncols]):
        return ns
    if pos[0]-1 >= 0:
        upper_n = pos[0]-1, pos[1]
        ns.append(upper_n)
    if pos[0]+1 < nrows:
        bottom_n = pos[0]+1, pos[1]
        ns.append(bottom_n)
    if pos[1]-1 >= 0:
        left_n = pos[0], pos[1]-1
        ns.append(left_n)
    if pos[1]+1 < ncols:
        right_n = pos[0], pos[1]+1
        ns.append(right_n)
    return ns

# найти путь:
# найти соседей текущей позиции
# выбрать свободных соседей
# обновить позицию любым свободным соседом
# а что если не будет ни одного свободного соседа?
# вернуться на предыдущий шаг
# то есть здесь по идее может быть дерево
# список шагов (если тупик, то можно вернуться к предыдущей позиции??)