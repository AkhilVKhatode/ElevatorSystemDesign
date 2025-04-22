from enums import FloorNumber
from panels import OutsidePannel

class Floor:
    def __init__(self, floor_number=None, outside_pannel=None):
        self.floor_number = floor_number
        self.outside_pannel = outside_pannel