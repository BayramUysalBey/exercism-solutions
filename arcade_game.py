"""In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game.

You have four rules to implement, all related to the game states.

Do not worry about how the arguments are derived, just focus on combining the arguments to return the intended result.

Task 1
Define the eat_ghost() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man is able to eat a ghost. The function should return True only if Pac-Man has a power pellet active and is touching a ghost.

>>> eat_ghost(False, True)
...
False

Task 2
Define the score() function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot) and returns a Boolean value if Pac-Man scored. The function should return True if Pac-Man is touching a power pellet or a dot.

>>> score(True, True)
...
True

Task 3
Define the lose() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man loses. The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.

>>> lose(False, True)
...
True

Task 4
Define the win() function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man wins. The function should return True if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.

>>> win(False, True, False)
...
False
"""

# My solution
def eat_ghost(has_power_pellet, touching_ghost):
  """Returns True if Pac-Man can eat the ghost, False otherwise."""
  return has_power_pellet and touching_ghost

def score(touching_power_pellet, touching_dot):
  """Returns True if Pac-Man scored, False otherwise."""
  return touching_power_pellet or touching_dot

def lose(has_power_pellet, touching_ghost):
  """Returns True if Pac-Man loses, False otherwise."""
  return touching_ghost and not has_power_pellet

def win(has_eaten_all_dots, has_power_pellet, touching_ghost):
  """Returns True if Pac-Man wins, False otherwise."""
  return has_eaten_all_dots and not lose(has_power_pellet, touching_ghost)