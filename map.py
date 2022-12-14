class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Map:

    def __init__(self):
        self.reset()

    def reset(self):
        
        self.grid = [ #y
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ], #x
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ]
        ]

    def set_character_position(self, character, clear = False):
     self.grid[character.position.y][character.position.x] = '.' if clear else 'X'

    def get_grid_square(self, point):
        return self.grid[point.y][point.x]

    def view(self):
        for row in self.grid:
            print(' '.join(row))