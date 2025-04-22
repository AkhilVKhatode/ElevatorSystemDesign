from enums import DoorAction, FloorNumber, Direction
from interfaces import Button

class DoorButton(Button):
    def __init__(self, status=False, door_action=None):
        self.status = status
        self.door_action = door_action

    def is_pressed(self):
        return self.status

    def press(self):
        self.status = not self.status
        return self.status

class ElevatorButton(Button):
    def __init__(self, status=False, floor_number=None):
        self.status = status
        self.floor_number = floor_number

    def is_pressed(self):
        return self.status

    def press(self):
        self.status = not self.status
        return self.status

class HallButton(Button):
    def __init__(self, status=False, direction=None):
        self.status = status
        self.direction = direction

    def is_pressed(self):
        return self.status

    def press(self):
        self.status = not self.status
        return self.status