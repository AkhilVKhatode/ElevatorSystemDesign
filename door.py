from enums import DoorAction

class Door:
    def __init__(self, door_action=None):
        self.door_action = door_action

    def open_door(self):
        self.door_action = DoorAction.OPEN

    def close_door(self):
        self.door_action = DoorAction.CLOSE