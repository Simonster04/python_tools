#time complexity O(n*m)
def is_subset(list1, list2):
    for elem in list1:
        if not elem in list2:
            return False
    return True

#improved O(n)
def is_subset_imp(list1, list2):
    temp = dict()
    for elem in list2:
        temp[elem] = 1
    for elem in list1:
        if not elem in list2:
            return False
    return True

#most improved O(n) (less lines)
def is_subset_mimp(list1, list2):
    temp = dict([(elem, 1) for elem in list2])
    for elem in list1:
        if not elem in list2:
            return False
    return True

print(is_subset_mimp([1,2,3,4,7,'a'], ['b',1,2,3,4,7]))