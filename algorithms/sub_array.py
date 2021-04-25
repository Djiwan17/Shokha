def max_sum_part(my_list):
    max_sum = 0
    list_length = len(my_list)
    r_border = list_length + 1
    for i in range(list_length):
        for j in range(i + 1, r_border):
            sum_part = sum(my_list[i:j]):
            if sum_part > max_sum:
                max_sum, left, right = sum_part, i, j - 1
    return (max_sum, left, right)
