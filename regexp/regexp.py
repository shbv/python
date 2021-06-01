"""
Supported using library "re". 
Faster than regular python text parsing since its compiled down & executed in C
"""

import re

"""
meta characters: 
    ^$ - anchor
    *+?{} - number of times
    [] - character class
    |()
"""

# e.g 1
text = 'abcdecdef'
match = re.search('^ab?[c-e]*', text)
print(f"match: {match}")
print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns abcdecde
print()

# e.g 2
text = 'abcdecdef'
match = re.search('^ab?[c-e]{1,2}', text)
print(f"match: {match}")
print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns abcd
print()

# e.g 3
text = 'abcdecdef'
match = re.search('^ab?[\w]*', text)  # \w escape code is for any alphanumeric, \W escape code is for non alphanumeric
print(f"match: {match}")
print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns abcdecdef

# e.g 4
text = 'abcdecdef'
match = re.search('^ab?[\d]+', text)    # \d escape code is for any digit, \D escape code is for non digit
print(f"match: {match}")
if match:
    print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns None
print()

# e.g 5
text = 'Test for regexp one two one'
string = 'one'
match = re.search(string, text)
print(f"match: {match}")
print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns one (first match)
print()

# e.g 6
text = 'Test for regexp one two one'
string = 'four'
regexp = re.compile(string)
match = re.search(regexp, text)
print(f"match: {match}")
if match:
    print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns None
print()

# e.g 7
text = 'Test for regexp one two one'
string = 'test'
regexp = re.compile(string, re.I) # case insensitive
match = re.search(regexp, text)
print(f"match: {match}")
if match:
    print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns None
print()

# e.g 8
text = 'uid@domain.com'
regexp = re.compile('''
                    [\w\.-]+    # username
                    @
                    [\w-]+    # domainname
                    ''',    
                    re.VERBOSE)  # multiline pattern with debug comments
match = re.search(regexp, text)
print(f"match: {match}")
if match:
    print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns None
print()

# e.g 9
text = 'Test for regexp one two One'
string = 'one'
regexp = re.compile(string, re.I)   # case insensitive
matches = re.findall(regexp, text)  # multiple matches - approach 1
print(f"matches: {matches}")
for match in matches:
    print(f"match: {match}")
print()
matches = re.finditer(regexp, text) # multiple matches - approach 2
print(f"matches: {matches}")
for match in matches:
    if match:
        print(f"match.group(): {match.group()}, match.start(): {match.start()}, match.end(): {match.end()}, match.span(): {match.span()}")
# returns None
print()


