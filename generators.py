"""Conda Airlines is the programming-world's biggest airline, with over 10,000 flights a day!

They are currently assigning all seats to passengers by hand; this will need to be automated.

They have asked you to create software to automate passenger seat assignments. They require your software to be memory efficient and performant.

Task 1
Conda wants to generate seat letters for their airplanes. An airplane is made of rows of seats. Each row has 4 seats. The seats in each row are always named A, B, C, and D. The first seat in the row is A, the second seat in the row is B, and so on. After reaching D, it should start again with A.

Implement a function generate_seat_letters(<number>) that accepts an int that holds how many seat letters to be generated. The function should then return an iterable of seat letters.

>>> letters = generate_seat_letters(4)
>>> next(letters)
"A"
>>> next(letters)
"B"

Task 2
Conda wants a system that can generate a given number of seats for their airplanes. Each airplane has 4 seats in each row. The rows are defined using numbers, starting from 1 and going up. The seats should be ordered, like: 1A, 1B, 1C, 1D, 2A, 2B, 2C, 2D, 3A, 3B, 3C, 3D, ...

Here is an example:

x	1	2
Row	5	21
Seat letter	A	D
Result	5A	21D
Many airlines do not have row number 13 on their flights, due to superstition amongst passengers. Conda Airlines also follows this convention, so make sure you don't generate seats for row number 13.

Implement a function generate_seats(<number>) that accepts an int that holds how many seats to be generated. The function should then return an iterable of seats given.

>>> seats = generate_seats(10)
>>> next(seats)
"1A"
>>> next(seats)
"1B"

Task 3
Now that you have a function that generates seats, you can use it to assign seats to passengers.

Implement a function assign_seats(<passengers>) that accepts a list of passenger names. The function should then return a dictionary of passenger as key, and seat_number as value.

>>> passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']

>>> assign_seats(passengers)
{'Jerimiah': '1A', 'Eric': '1B', 'Bethany': '1C', 'Byte': '1D', 'SqueekyBoots': '2A', 'Bob': '2B'}

Task 4
Conda Airlines would like to have a unique code for each ticket. Since they are a big airline, they have a lot of flights. This means that there are multiple flights with the same seat number. They want you to create a system that creates a unique ticket that is 12 characters long string code for identification.

This code begins with the assigned_seat followed by the flight_id. The rest of the code is appended by 0s.

Implement a function generate_codes(<seat_numbers>, <flight_id>) that accepts a list of seat_numbers and a string with the flight number. The function should then return a generator that yields a ticket_number.

>>> seat_numbers = ['1A', '17D']
>>> flight_id = 'CO1234'
>>> ticket_ids = generate_codes(seat_numbers, flight_id)

>>> next(ticket_ids)
'1ACO12340000'
>>> next(ticket_ids)
'17DCO1234000'
"""

# My solution
"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ["A","B","C","D"]
    letter_index = 0
    for i in range(number):
	    yield letters[letter_index % 4]
        letter_index += 1



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_letters = ['A', 'B', 'C', 'D']
    row_number = 1
    seats_generated = 0
    while seats_generated < number:
        if row_number != 13:
            for letter in seat_letters:
                if seats_generated < number:
                    yield f"{row_number}{letter}"
                    seats_generated += 1
                else:
                    break  # Stop generating if we've reached the desired number
        row_number += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    num_passengers = len(passengers)
    seat_generator = generate_seats(num_passengers)
    assignment = {}
    for passenger in passengers:
        try:
            seat = next(seat_generator)
            assignment[passenger] = seat
        except StopIteration:
            print("Error: Not enough seats generated for all passengers.")
            break  
    return assignment

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        base_code = seat + flight_id
        padding_needed = 12 - len(base_code)
        if padding_needed < 0:
            yield base_code[:12]  
        else:
            padding = '0' * padding_needed
            yield base_code + padding