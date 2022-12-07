from Character import Character
from map import Map, Point

flo = Character('FlyingFlumer', 'Flo', ['food', 'sword', 'silly stones'], can_teleport=True, position=Point(5,6), token='F')
map = Map([flo])

map.view()

flo.run('west', map)

map.view()