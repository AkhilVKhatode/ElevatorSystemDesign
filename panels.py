from buttons import ElevatorButton, DoorButton, HallButton
from enums import FloorNumber, DoorAction, Direction
from interfaces import Pannel

class InsidePannel(Pannel):
    def __init__(self):
        self.elevator_button_list = [ElevatorButton(False, fn) for fn in FloorNumber]
        self.door_buttons = [DoorButton(False, da) for da in DoorAction]

    def press_floor_button(self, floor_number):
        return self.elevator_button_list[floor_number].press()

    def press_door_button(self, door_number):
        return self.door_buttons[door_number].press()

class OutsidePannel(Pannel):
    def __init__(self):
        self.hall_buttons = [
            HallButton(False, Direction.UP),
            HallButton(False, Direction.DOWN),
            HallButton(False, Direction.IDLE)
        ]