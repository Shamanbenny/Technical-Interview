"""
Is Unique:  Implement an algorithm to determine if a string has all unique characters.
            What if you cannot use additional data structures?
"""
def isUnique1(string: str) -> bool:
  return len(string) == len(set(string))

def isUnique2(string: str) -> bool:
    # Solution using only List() instead of Set()
    seen = []
    for char in string:
        if char in seen:
            return False
        seen.append(char)
    return True


print('isUnique1("Hello World!"): ' + str(isUnique1("Hello World!")))
print('isUnique1("asdfghjkl1234567890"): ' + str(isUnique1("asdfghjkl1234567890")))

print('isUnique2("Hello World!"): ' + str(isUnique2("Hello World!")))
print('isUnique2("asdfghjkl1234567890"): ' + str(isUnique2("asdfghjkl1234567890")))