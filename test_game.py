class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


import pytest

def test_room():
    gold = Room("GoldRoom", 
                           """This room has gold in it you can grab, 
                              There is a door to the north,""")

    assert gold.name == "GoldRoom"
    assert gold.paths == {}

@pytest.fixture()
def test_add_paths():
    center = Room("Center", 'i mitten')

    center.add_paths(['north'] = north)


def test_stigen(test_add_paths):
    paths == 'north'
