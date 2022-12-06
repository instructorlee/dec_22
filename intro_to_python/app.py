characters = [ 
    {   
        "type": "FuzzBall",
        "name": "Fred",
        "power_points": 5,
        "can_teleport": False,
        "inventory": ['food', 'fireball', 'shield']
    },
    {
        "type": "BeatleBop",
        "name": "Betty",
        "power_points": 1,
        "can_teleport": True,
        "inventory": ['food', 'sword', 'silly stones'] 
    }
]

is_active = True

def get_character(character_name):

    for character in characters:
        if character['name'] == character_name: 
            return character

    return None

def do_action(action, character):

    type, name, power_points, can_teleport, inventory = character.values()

    if action == 'run':

        if power_points >= 2:
            print( f'{name} is running.')
            power_points -= 2

        else:
            print( f'{name} only has {power_points} Power Points and cannot run.')

    elif action == 'rest':
        
        if power_points < 10:
            print( f'{name} is resting.')
            power_points += 1

        else:
            print( f'{name} has {power_points} Power Points and does not need to rest.')

    elif action == 'teleport':
        
        if power_points >= 4 and can_teleport:
            print( f'{name} is teleporting.')
            power_points -= 4

        elif power_points < 4:
            print( f'{name} only has {power_points} Power Points and cannot teleport.')

        else:
            print( f'{name} is not able to teleport.')

    elif action == 'inventory':

        for item in inventory:
                print ( item )

    else:
        print ( "Invalid action")

def reset_characters():
    for character in characters:
        character['power_points'] = 10

def update_character_inventory(character, item):
    character['inventory'].append(item)

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

    character = get_character(command)

    if character is None:
        print("invalid character")
        continue

    do_action(action, character)
    