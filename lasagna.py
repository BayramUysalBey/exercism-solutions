'''You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

You have five tasks, all related to cooking your recipe.


Note
We have started the first function definition for you in the stub file, but you will need to write the remaining function definitions yourself. You will also need to define any constants yourself. Read the #TODO comment lines in the stub file carefully. Once you are done with a task, remove the TODO comment.

Task 1
Define the EXPECTED_BAKE_TIME constant that represents how many minutes the lasagna should bake in the oven. According to your cookbook, the Lasagna should be in the oven for 40 minutes:

>>> print(EXPECTED_BAKE_TIME)
40

Task 2
Complete the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME constant.

>>> bake_time_remaining(30)
10

Task 3
Define the preparation_time_in_minutes() function that takes the number_of_layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

>>> def preparation_time_in_minutes(number_of_layers):
        ...
        ...
        
>>> preparation_time_in_minutes(2)
4

Task 4
Define the elapsed_time_in_minutes() function that takes two parameters as arguments:

number_of_layers (the number of layers added to the lasagna)
elapsed_bake_time (the number of minutes the lasagna has spent baking in the oven already).
This function should return the total minutes you have been in the kitchen cooking — your preparation time layering + the time the lasagna has spent baking in the oven.

>>> def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
        ...
        ...
        
>>> elapsed_time_in_minutes(3, 20)
26

Task 5
Go back through the recipe, adding "notes" in the form of function docstrings.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
'''

# My solution
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(actual_bake_time):
    """
    Calculates the remaining baking time for the lasagna.

    Args:
        actual_bake_time (int): The actual minutes the lasagna has been in the oven.

    Returns:
        int: The remaining minutes the lasagna needs to bake.
    """
    return EXPECTED_BAKE_TIME - actual_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Calculates the total preparation time for adding layers to the lasagna.

    Args:
        number_of_layers (int): The number of layers to be added to the lasagna.

    Returns:
        int: The total minutes spent preparing the layers.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculates the total elapsed cooking time for the lasagna.

    Args:
        number_of_layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has been baking in the oven.

    Returns:
        int: The total minutes spent cooking.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time