import random
from enums import Direction, FloorNumber, ElevatorNumber
from elevator import Elevator
from floor import Floor
from door import Door
from panels import InsidePannel, OutsidePannel
from display import Display

class ElevatorSystem:
    _instance = None

    def __init__(self):
        self.elevators = [
            Elevator(ElevatorNumber.ELEVATOR_NUMBER1, Door(), InsidePannel(), Display(), FloorNumber.FLOOR_NUMBER1, Direction.IDLE),
            Elevator(ElevatorNumber.ELEVATOR_NUMBER2, Door(), InsidePannel(), Display(), FloorNumber.FLOOR_NUMBER1, Direction.IDLE),
            Elevator(ElevatorNumber.ELEVATOR_NUMBER3, Door(), InsidePannel(), Display(), FloorNumber.FLOOR_NUMBER1, Direction.IDLE)
        ]
        self.floors = [Floor(fn, OutsidePannel()) for fn in FloorNumber]

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ElevatorSystem()
        return cls._instance

    def request_elevator(self, direction, floor):
        idle_elevators = [e for e in self.elevators if e.current_direction == Direction.IDLE]
        selected = idle_elevators[0] if idle_elevators else random.choice(self.elevators)
        print(f"Dispatching Elevator: {selected.elevator_number.name} to Floor: {floor.floor_number.name}")
        selected.current_direction = direction
        selected.current_floor_number = floor.floor_number
        return selected

    def open_door(self, elevator):
        elevator.door.open_door()
        print(f"Elevator {elevator.elevator_number.name} door opened.")

    def close_door(self, elevator):
        elevator.door.close_door()
        print(f"Elevator {elevator.elevator_number.name} door closed.")

    def select_floor(self, floor_number, elevator):
        print(f"Floor {floor_number.name} selected in {elevator.elevator_number.name}")
        elevator.inside_pannel.press_floor_button(floor_number.value - 1)