'''Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.'''

# My solution
def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-","")
    if string is None:
         return True
    seen = set()
    for char in string:
            if char in seen:
                return False
            else:
                seen.add(char)
    return True