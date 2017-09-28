class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


center_room = Room('center', 'In the middle')
north_room = Room('north', 'a room facing north')
south_room = Room('south', 'the room with a balcony')

north_room.add_paths({'south': center_room})
center_room.add_paths({'north': north_room})
center_room.add_paths({'south': south_room})
south_room.add_paths({'north': center_room})

my_room = north_room.go('south')
print 'I am in', my_room.name

my_room = my_room.go('south')
print 'I am in', my_room.name

my_room= my_room.go('north')
my_room= my_room.go('north')
print 'I am in', my_room.name
