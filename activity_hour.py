"""
SPECS

    Implement Map class

"""

from Character import Character
from map import Map, Point

player = Character('FuzzBall', ['food', 'fireball', 'shield'], can_teleport=True, position=Point(8,2))

is_active = True
map = Map()
map.set_character_position(player)

def get_character(character_name):

    for character in Character.all_characters:
        if character.name == character_name:
            return character

    return None

def do_action(action, direction, character):

    if action == 'run':

        character.run(direction, map)

    elif action == 'rest':
        
        character.rest()

    elif action == 'teleport':
        
        character.teleport()

    elif action == 'inventory':

        character.list_inventory()

    else:
        print ( "Invalid action")

while is_active:

    line_input = input('command? ').strip()

    if line_input == "":
        continue

    line_parts = (line_input + "  ").split(" ")

    command = line_parts[0]
    action = line_parts[1]
    extra = line_parts[2]

    if command == 'quit':
        is_active = False
        continue

    elif command == 'view-map':
        map.view()
        continue

    character = get_character(command)

    if character is None:
        print("invalid character")
        continue

    do_action(action, extra, character)
    