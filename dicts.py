"""In this exercise, you will be managing an inventory system.

The inventory should be organized by the item name and it should keep track of the number of items available.

You will have to handle adding items to an inventory. Each time an item appears in a given list, the item's quantity should be increased by 1 in the inventory. You will also have to handle deleting items from an inventory by decreasing quantities by 1 when requested.

Finally, you will need to implement a function that will return all the key-value pairs in a given inventory as a list of tuples.

Task 1
Implement the create_inventory(<input list>) function that creates an "inventory" from an input list of items. It should return a dict containing each item name paired with their respective quantity.

>>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
{"coal":1, "wood":2, "diamond":3}

Task 2
Implement the add_items(<inventory dict>, <item list>) function that adds a list of items to the passed-in inventory:

>>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
{"coal":2, "wood":2, "iron":1}

Task 3
Implement the decrement_items(<inventory dict>, <items list>) function that takes a list of items. Your function should remove 1 from an item count for each time that item appears on the list:

>>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
{"coal":2, "diamond":0, "iron":3}
Item counts in the inventory should not be allowed to fall below 0. If the number of times an item appears on the input list exceeds the count available, the quantity listed for that item should remain at 0. Additional requests for removing counts should be ignored once the count falls to zero.

>>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}

Task 4
Implement the remove_item(<inventory dict>, <item>) function that removes an item and its count entirely from an inventory:

>>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
{"wood":1, "diamond":2}
If the item is not found in the inventory, the function should return the original inventory unchanged.

>>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
{"coal":2, "wood":1, "diamond":2}

Task 5
Implement the list_inventory(<inventory dict>) function that takes an inventory and returns a list of (item, quantity) tuples. The list should only include the available items (with a quantity greater than zero):

>>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
"""

# My solution
"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = {}
    for item in items:
      if item in inventory:
        inventory[item] += 1
      else:
        inventory[item] = 1
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)
    
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    inventory_list = []
    for item, quantity in inventory.items():
        if quantity > 0:
            inventory_list.append((item, quantity))
    return inventory_list