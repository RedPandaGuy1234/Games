import Locations
Current_Coordinate = 0
Patrol_Boat = [0, 0]
Battleship = [0, 0, 0, 0]
Destroyer = [0, 0, 0]
Sumbarine = [0, 0, 0]
Carrier = [0, 0, 0, 0, 0]

col_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def check_coordinates_answer(Coordinate):
    if Coordinate[0] in col_letters and Coordinate[1:].isdigit():
        return True
    else:
        return False


Current_Coordinate = input(
    "Let's get started! What is the first coordinate you want your patrol boat (2 squares)? "
    "Each coordinate starts with A to J (please use uppercase), then 1 to 10 with no spaces: "
)

if check_coordinates_answer(Current_Coordinate):
    print("Valid coordinate!")
    Patrol_Boat[0] = Current_Coordinate
else:
    print("Invalid coordinate!")
