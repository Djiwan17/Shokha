def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_list = lst[:middle]
    right_list = lst[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))


def merge(left_half, right_half):
    r = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            r.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            r.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        r += right_half
    else:
        r += left_half
    return r


lst = [12, 34, 23, 14, 7, 23, 8, 5, 74]
print("Ввод: ", lst)
result = merge_sort(lst)
print("Вывод: ", result)
