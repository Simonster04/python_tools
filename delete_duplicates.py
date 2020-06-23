# worst case O(n²)
def del_duplicates_w(array):
    result = []
    for val in array:
        if not val in result:
            result.append(val)
    return result

# better case: hash tables O(n) (python dictionaries are like hash tables)
def del_duplicates_b(array):
    result = {}
    for val in array:
        if not val in result:
            result[val] = 1
    return list(result.keys())


print(del_duplicates_b([1, 2, 3, 4]))