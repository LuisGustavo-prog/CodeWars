# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

from collections import Counter

def duplicate_count(text):
    character_counter, number_of_repeated_characters = Counter(text.lower()), 0
    
    for character, number in character_counter.items():
        if number > 1:
            number_of_repeated_characters += 1
    
    return number_of_repeated_characters


print(duplicate_count(text='abcde')) # 0
print(duplicate_count(text='abcdea')) # 1
print(duplicate_count(text='aabbcde')) # 2

