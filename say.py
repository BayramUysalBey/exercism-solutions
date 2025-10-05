"""Given a number, your task is to express it in English words exactly as your friend should say it out loud. Yaʻqūb expects to use numbers from 0 up to 999,999,999,999.

Examples:

0 → zero
1 → one
12 → twelve
123 → one hundred twenty-three
1,234 → one thousand two hundred thirty-four
Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

This particular exercise requires that you use the raise statement to "throw" a ValueError if the number input to say() is out of range. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

# if the number is negative
raise ValueError("input out of range")

# if the number is larger than 999,999,999,999
raise ValueError("input out of range")"""

# My solution
def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def chunk_to_words(n):
        word = ""
        hundred = n // 100
        rem = n % 100

        if hundred > 0:
            word += ones[hundred] + " hundred"
            if rem > 0:
                word += " "

        if rem >= 20:
            word += tens[rem // 10]
            if rem % 10 > 0:
                word += "-" + ones[rem % 10]
        elif rem >= 10:
            word += teens[rem - 10]
        elif rem > 0:
            word += ones[rem]

        return word

    words = []
    for i in range(len(thousands)):
        part = number % 1000
        number //= 1000
        if part > 0:
            chunk_word = chunk_to_words(part)
            if thousands[i]:
                chunk_word += " " + thousands[i]
            words.append(chunk_word)

    return " ".join(reversed(words))