class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

def test_room():
    gold = Room("GoldRoom", 
                           """This room has gold in it you can grab, 
                              There is a door to the north,""")

    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_add_paths():
    pass
    center_room = Room("Center", "Test room in the center")
    north_room = Room("North", "Test room in the north")
    south_room = Room("South", "Test room in the south")

    north_room.add_paths({'south': south_room})
    center_room.add_paths({'north': north_room})
    center_room.add_paths({'south': south_room})
    south_room.add_paths({'north': center_room})


    riktning = north_room.go('south')
    assert riktning.name == 'South'
    riktning = riktning.go('north')
    assert riktning.name == 'Center'
    riktning = riktning.go('north')
    assert riktning.name == 'North'
    # riktning == direction in English
