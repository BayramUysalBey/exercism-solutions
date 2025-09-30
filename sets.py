"""You and your business partners operate a small catering company. You've just agreed to run an event for a local cooking club that features "club favorite" dishes. The club is inexperienced in hosting large events, and needs help with organizing, shopping, prepping and serving. You've decided to write some small Python scripts to speed the whole planning process along.

Task 1
The event recipes were added from various sources and their ingredients appear to have duplicate (or more) entries — you don't want to end up purchasing excess items! Before the shopping and cooking can commence, each dish's ingredient list needs to be "cleaned".

Implement the clean_ingredients(<dish_name>, <dish_ingredients>) function that takes the name of a dish and a list of ingredients. This function should return a tuple with the name of the dish as the first item, followed by the de-duped set of ingredients.

>>> clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

>>> ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})

Task 2
The event is going to include both cocktails and "mocktails" - mixed drinks without the alcohol. You need to ensure that "mocktail" drinks are truly non-alcoholic and the cocktails do indeed include alcohol.

Implement the check_drinks(<drink_name>, <drink_ingredients>) function that takes the name of a drink and a list of ingredients. The function should return the name of the drink followed by "Mocktail" if the drink has no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol. For the purposes of this exercise, cocktails will only include alcohols from the ALCOHOLS constant in sets_categories_data.py:

>>> from sets_categories_data import ALCOHOLS 

>>> check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
...
'Honeydew Cucumber Mocktail'

>>> check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])
...
'Shirley Tonic Cocktail'

Task 3
The guest list includes diners with different dietary needs, and your staff will need to separate the dishes into Vegan, Vegetarian, Paleo, Keto, and Omnivore.

Implement the categorize_dish(<dish_name>, <dish_ingredients>) function that takes a dish name and a set of that dish's ingredients. The function should return a string with the dish name: <CATEGORY> (which meal category the dish belongs to). All dishes will "fit" into one of the categories imported from sets_categories_data.py (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

>>> from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE


>>> categorize_dish('Sticky Lemon Tofu', {'tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar'})
...
'Sticky Lemon Tofu: VEGAN'

>>> categorize_dish('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', {'shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt', 'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion'})
...
'Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole: OMNIVORE'

Task 4
Some guests have allergies and additional dietary restrictions. These ingredients need to be tagged/annotated for each dish so that they don't cause issues.

Implement the tag_special_ingredients(<dish>) function that takes a tuple with the dish name in the first position, and a list or set of ingredients for that dish in the second position. Return the dish name followed by the set of ingredients that require a special note on the dish description. Dish ingredients inside a list may or may not have duplicates. For the purposes of this exercise, all allergens or special ingredients that need to be labeled are in the SPECIAL_INGREDIENTS constant imported from sets_categories_data.py.

>>> from sets_categories_data import SPECIAL_INGREDIENTS

>>> tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice']))
...
('Ginger Glazed Tofu Cutlets', {'garlic','soy sauce','tofu'})

>>> tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts', 'balsamic vinegar', 'onions', 'black pepper']))
...
('Arugula and Roasted Pork Salad', {'pork tenderloin', 'blue cheese', 'pine nuts', 'onions'})

Task 5
In preparation for ordering and shopping, you'll need to compile a "master list" of ingredients for everything on the menu (quantities to be filled in later).

Implement the compile_ingredients(<dishes>) function that takes a list of dishes and returns a set of all ingredients in all listed dishes. Each individual dish is represented by its set of ingredients.

dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]

>>> compile_ingredients(dishes)
...
{'arugula', 'brown sugar', 'honeydew', 'coconut water', 'english cucumber', 'balsamic vinegar', 'mint leaves', 'pears', 'pork tenderloin', 'ginger', 'blue cheese', 'soy sauce', 'sesame seeds', 'black pepper', 'garlic', 'lime juice', 'corn starch', 'pine nuts', 'lemon juice', 'onions', 'salt', 'tofu'}

Task 6
The hosts have given you a list of dishes they'd like prepped as "bite-sized" appetizers to be served on trays. You need to pull these from the main list of dishes being prepared as larger servings.

Implement the separate_appetizers(<dishes>, <appetizers>) function that takes a list of dish names and a list of appetizer names. The function should return the list of dish names with appetizer names removed. Either the <dishes> or <appetizers> list could contain duplicates and may require de-duping.

dishes =    ['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
             'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
             'Barley Risotto','Kingfish Lettuce Cups']
          
appetizers = ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
              'Asparagus Puffs']
              
>>> separate_appetizers(dishes, appetizers)
...
['Vegetarian Khoresh Bademjan', 'Barley Risotto', 'Flank Steak with Chimichurri and Asparagus', 
 'Grilled Flank Steak with Caesar Salad']

 Task 7
 Within each category (Vegan, Vegetarian, Paleo, Keto, Omnivore), you're going to pull out ingredients that appear in only one dish. These "singleton" ingredients will be assigned a special shopper to ensure they're not forgotten in the rush to get everything else done.

Implement the singleton_ingredients(<dishes>, <INTERSECTIONS>) function that takes a list of dishes and a <CATEGORY>_INTERSECTIONS constant for the same category. Each dish is represented by a set of its ingredients. Each <CATEGORY>_INTERSECTIONS is a set of ingredients that appear in more than one dish in the category. Using set operations, your function should return a set of "singleton" ingredients (ingredients appearing in only one dish in the category).

from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION

>>> singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION)
...
{'garlic powder', 'sunflower oil', 'mixed herbs', 'cornstarch', 'celeriac', 'honey', 'mushrooms', 'bell pepper', 'rosemary', 'parsley', 'lemon', 'yeast', 'vegetable oil', 'vegetable stock', 'silken tofu', 'tofu', 'cashews', 'lemon zest', 'smoked tofu', 'spaghetti', 'ginger', 'breadcrumbs', 'tomatoes', 'barley malt', 'red pepper flakes', 'oregano', 'red onion', 'fresh basil'}
"""

# My solution
"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return (dish_name, set(dish_ingredients))



def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    has_alcohol = False
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            has_alcohol = True
            break

    if has_alcohol:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    elif dish_ingredients.issubset(OMNIVORE):
        return f"{dish_name}: OMNIVORE"
    else:
        
        return f"{dish_name}: UNCATEGORIZED"


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    dish_name, ingredients = dish

   
    ingredient_set = set(ingredients)

    special_ingredients_in_dish = ingredient_set.intersection(SPECIAL_INGREDIENTS)

    return (dish_name, special_ingredients_in_dish)


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    master_ingredients = set()
    for dish_ingredients in dishes:
        master_ingredients.update(dish_ingredients)
    return master_ingredients


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    unique_dishes = set(dishes)
    unique_appetizers = set(appetizers)
    remaining_dishes = unique_dishes.difference(unique_appetizers)
    return list(remaining_dishes)

def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    all_ingredients = set()
    common_ingredients = set(intersection)
    for dish in dishes:
        all_ingredients.update(dish)
    singleton_ingredients = all_ingredients - common_ingredients
    return singleton_ingredients