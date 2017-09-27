class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


center = Room('Center', 'I mitten')
norr = Room('norr', 'Ett rum norrut')
south = Room('south', 'the room with a balcony')

print norr.name
print norr.description
print norr.paths

h = {'norr': norr}
norr.add_paths(h)
norr.go(center)
print norr.paths
print norr.go
