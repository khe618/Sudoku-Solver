def get_column(arr, i):
    column = []
    for row in arr:
        column.append(row[i])
    return set(column)
def get_box(arr, i, j):
    box = []
    y_bound = i - (i % 3)
    x_bound = j - (j % 3)
    for m in range(y_bound, y_bound + 3):
        for n in range(x_bound, x_bound + 3):
            box.append(arr[m][n])
    return set(box)

arr = [[4, 0, 0, 0, 0, 6, 0, 0, 0],
       [0, 6, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 6, 0, 0, 2, 0],
       [1, 0, 0, 0, 0, 0, 9, 0, 0],
       [8, 0, 0, 0, 0, 5, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 5]]
numbers = {1,2,3,4,5,6,7,8,9}
arr_initial = [x[:] for x in arr]
index = 0
forward = True
possible_nums = [0] * 81
while index < 81:
    print(index)
    if forward:
        if arr_initial[index // 9][index % 9] != 0:
            index += 1
        else:
            possible_numbers = list(numbers - set(arr[index // 9]) - get_column(arr, index % 9) - 
                                  get_box(arr, index // 9, index % 9))
            print(possible_numbers)
            if len(possible_numbers) > 0:
                arr[index // 9][index % 9] = possible_numbers.pop()
                possible_nums[index] = possible_numbers
                index += 1
            else:
                forward = False
                index -= 1
    else:
        if arr_initial[index // 9][index % 9] != 0:
            index -= 1
        elif len(possible_nums[index]) > 0:
            arr[index // 9][index % 9] = possible_nums[index].pop()
            forward = True
            index += 1
        else:        
            arr[index // 9][index % 9] = 0
            index -= 1
print(arr)
