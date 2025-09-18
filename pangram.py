"""Your task is to figure out if a sentence is a pangram.

A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet."""

# My solution
def is_pangram(sentence):
		f = 0
		for char in sentence.lower():
			if char.isalpha():
				f |= 1 << (ord(char) - ord("a"))
			if f == (1 << 26) - 1:
				return True
				break
		else:
			return False