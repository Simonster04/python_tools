# [1,2,3,5,6] => 4

#complexity O(n*m)
def missing_num(list_int):
    for i in range(1, len(list_int)):
        if not i in list_int:
            return i
    return -1

# lower complexity
def missing_num_b(list_int):
    for i in range(1, len(list_int)):
        if not i == list_int[i - 1]: #works because list is sorted
            return i
    return -1

#best option: recursion
def missing_num_r(list_int, start, end):
    print(start)
    if start == end:
        return start + 1
    mid_index = int((start + end) / 2)
    if list_int[mid_index] == mid_index + 1:
        missing_num_r(list_int, mid_index + 1, end)
    else:
        missing_num_r(list_int, start, mid_index - 1)


print(missing_num_r([1, 2, 3, 5, 6], 0, 5))