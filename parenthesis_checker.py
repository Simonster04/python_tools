# ((()())()) => True
# )())()) => False
# ((()( => False

def check(string):
    left = 0
    for char in string:
        if char == '(':
            left += 1
        else:
            if left == 0:
                return False
            left -= 1
    return left == 0

print(check('((()())())'))
print(check(')())())'))
print(check('((()('))
print(check(')('))