# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return ''.join(list(filter(lambda x: x != '!', s)))

print(remove_exclamation_marks("Hello World!"))
