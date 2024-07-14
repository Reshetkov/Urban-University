my_list = [42, 69, 0, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
N = len(my_list)
while i <= N-1:
    if (my_list[i]) < 0:
        break
    if my_list[i] > 0:
        print(my_list[i])
        i += 1
    else:
        i += 1