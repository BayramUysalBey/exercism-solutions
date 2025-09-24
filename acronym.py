"""Convert a phrase to its acronym.

Techies love their TLA (Three Letter Acronyms)!

Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).

Punctuation is handled as follows: hyphens are word separators (like whitespace); all other punctuation can be removed from the input.

For example:

Input	                         Output
As Soon As Possible	             ASAP
Liquid-crystal display	         LCD
Thank George It's Friday!	     TGIF
"""

# My solution
def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ")
    return ''.join(word[0].upper() for word in words.split() if word[0].isalpha())