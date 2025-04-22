from enums import ElevatorNumber, FloorNumber, Direction
from door import Door
from panels import InsidePannel
from display import Display

class Elevator:
    def __init__(self, elevator_number=None, door=None, inside_pannel=None, display=None,
                 current_floor_number=None, current_direction=None):
        self.elevator_number = elevator_number
        self.door = door
        self.inside_pannel = inside_pannel
        self.display = display
        self.current_floor_number = current_floor_number
        self.current_direction = current_direction