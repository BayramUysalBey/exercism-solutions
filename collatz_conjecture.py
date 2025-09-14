"""Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

The Collatz Conjecture is only concerned with strictly positive integers, so this exercise expects you to use the raise statement and "throw" a ValueError in your solution if the given value is zero or a negative integer. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

# example when argument is zero or a negative integer
raise ValueError("Only positive integers are allowed")"""

# My solution
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    result = []
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        result.append(number)
    
    return len(result)