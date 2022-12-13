from Character import Character
from FlyingFlumer import FlyingFlumer
from map import Map, Point

flo_1 = Character('FlyingFlumer', 'Flo', ['food', 'sword', 'silly stones'], can_teleport=True, position=Point(5,6), token='F')
flo = FlyingFlumer("Flo", position=Point(4,4))

map = Map([flo])

map.view()

flo.fly('west', map)

map.view()