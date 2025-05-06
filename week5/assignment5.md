### Assignment 5
The goal of this week is to build an inventory management game. You're a character exploring a world (text-based). Along the way, you:
- Pick up and drop items
- Use or examine them
- Deal with inventory limits

Core features
1. Inventory System
  - A list holds your items: `inventory = []`
  - Each item is a dictionary: `{"name": "medicine", "type": "healing", "uses": 1}`
  - Inventory Limit: max of 5 items
2. Room System
  - A dictionary or a list of dictionary represents items in the current area: 
```
items_in_room = [
    {"name": "Key", "type": "tool"},
    {"name": "Apple", "type": "food"}
]
```
3. Actions 
  - Use functions to define the following basic actions:
```
def show_room_items(): ...
def pick_up(item_name): ...
def drop(item_name): ...
def use(item_name): ...
def show_inventory(): ...
def examine(item_name): ...
```
4. User Interactions
  - Users shall be able to navigate the game by typing commands in following ways
```
inventory
pickup apple
drop torch
use potion
examine sword
help
```
5. Define a meaningful scenario and goal for your little game, let it be a classic escape game, survival on an island, buying healthy food in a supermarket...

Bonus
- Multiple rooms that can activated/navigated if a certain item is obtained
- Events can be triggered by special items