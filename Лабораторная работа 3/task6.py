list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = 0
imax = 0
i = 0
for element in list_numbers:
    if list_numbers[i] > max_:
        max_ = element
        imax = i
    i += 1
list_numbers[imax], list_numbers[-1] = list_numbers[-1], list_numbers[imax]

print(list_numbers)
