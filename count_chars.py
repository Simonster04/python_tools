from collections import defaultdict

#hash tables improved O(n)
def count_chars(string):
    result = defaultdict(int)
    for char in string:
        result[char] += 1
    for key, val in result.items():
        print(key, val)

#hash tables without defaultdict O(n)
def count_chars(string):
    result = {}
    for char in string:
        result[char] = result.get(c, 0) + 1
    for key, val in result.items():
        print(key, val)

#hash tables O(n)
def count_chars(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    for key, val in result.items():
        print(key, val)

count_chars('aaadbnjsjojsojsy')