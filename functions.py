def d(first):
    def inner_d():
        nonlocal first #code works because of this line
        first += 1
        print(first)
    return inner_d


f = d(10)

f() #11 will be printed
f() #12 will be printed