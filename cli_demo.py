is_active = True

while is_active:

    line_input = input('Command? ').strip()

    print ( line_input ) # walk 3 west

    line_parts = (line_input + "  ").split(" ") # 'walk 3 west  '
    # line_parts = line_input.split(" ") # split('.') hello.world

    command = line_parts[0]
    extra_1 = line_parts[1]
    extra_2 = line_parts[2]

    if command == 'quit':
        print("Thank You for playing!")
        is_active = False
        
    elif command == 'walk': # walk 3 west, walk 15 north
        
        print(f'I am walking {extra_1} {extra_2} spaces.')

    elif command == 'cast-spell': # cast-spell fireball 3
        
        print(f'I am casting a {extra_1} spell with {extra_2} power.')

    else:
        print("Invalid Command")
      