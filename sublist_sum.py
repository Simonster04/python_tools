#if a have [1,2,3,5,4,5], 11 => [1 - 3] (the number index range in list that sum 11), -1 otherwise

def sublist_sum(list_int, sum):
    for i in range(len(list_int) - 1):
        interval_sum = list_int[i]
        if interval_sum == sum:
            print(i, i)
            return True
        for j in range(i + 1, len(list_int)):
            interval_sum += list_int[j]
            if interval_sum == sum:
                print(i, j)
                return True
            elif sum < interval_sum:
                break
    print(-1)
    return False

sublist_sum([1,2,5,4,5], 5)