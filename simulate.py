from system import ElevatorSystem
from enums import Direction, FloorNumber

system = ElevatorSystem.get_instance()
floor_request = system.floors[5]  # Floor 6
elevator = system.request_elevator(Direction.UP, floor_request)
system.open_door(elevator)
system.select_floor(FloorNumber.FLOOR_NUMBER10, elevator)
system.close_door(elevator)