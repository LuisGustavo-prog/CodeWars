# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

def get_middle(s):
    middle = len(s) / 2
    middle_int = int(middle)

    return s[middle_int] if middle % 1 > 0 else s[middle_int - 1: middle_int + 1]

print(get_middle("test")) # es
print(get_middle("testing")) # t 
