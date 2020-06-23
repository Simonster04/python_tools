def reverse_string(string):
    result = ""
    for char in string:
        resutl = char + result
    return result

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("aba"))
print(is_palindrome("abc"))