import random
def print_random(array):
    for i in range(len(array), 0, -1):
        index_to_del = random.randint(0, i - 1)
        print(array[index_to_del])
        del array[index_to_del]

#without del() (better)
def print_rand(array):
    for i in range(len(array), 0, -1):
        index_to_del = random.randint(0, i - 1)
        print(array[index_to_del])
        array[index_to_del] = array[i - 1]


print_rand([1,2,3,4,5,'a'])