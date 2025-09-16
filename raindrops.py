"""Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
Examples
28 is divisible by 7, but not 3 or 5, so the result would be "Plong".
30 is divisible by 3 and 5, but not 7, so the result would be "PlingPlang".
34 is not divisible by 3, 5, or 7, so the result would be "34"."""

# My solution
def convert(number):
	if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
		return "PlingPlangPlong"
	if number % 3 == 0 and number % 5 == 0:
		return "PlingPlang"
	elif number % 3 == 0 and number % 7 == 0:
		return "PlingPlong"
	elif number % 5 == 0 and number % 7 == 0:
		return "PlangPlong"	
	elif number % 3 == 0:
		return "Pling"
	elif number % 5 == 0:
		return "Plang"
	elif number % 7 == 0:
		return "Plong"
	else:
		return f"{str(number)}"