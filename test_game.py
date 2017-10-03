from Rooms import Room

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


    my_rooms = north_room.go('south')
    assert my_rooms.name == 'South'
    my_rooms = my_rooms.go('north')
    assert my_rooms.name == 'Center'
    my_rooms = my_rooms.go('north')
    assert my_rooms.name == 'North'
    
