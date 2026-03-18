# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

from collections import Counter

def xo(s):
    s_counter = Counter(s.lower())
    return s_counter['x'] == s_counter['o']

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo(s='ooxx')) # True
print(xo(s='xooxx')) # false
print(xo(s='zpzpzpp')) # true
