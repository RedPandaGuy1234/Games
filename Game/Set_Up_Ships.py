import Locations

Current_Coordinate = 0

Patrol_Boat = [0, 0]
Battleship = [0, 0, 0, 0]
Destroyer = [0, 0, 0]
Submarine = [0, 0, 0]
Carrier = [0, 0, 0, 0, 0]

col_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def check_coordinates_answer(Coordinate):
    if isinstance(Coordinate, str) and len(Coordinate) >= 2 and Coordinate[0] in col_letters and Coordinate[1:].isdigit():
        column_number = col_letters.index(Coordinate[0])
        row_number = int(Coordinate[1:])
        return (column_number, row_number)
    else:
        return None
#This is a test line below, and will be deleted.
print(Patrol_Boat[0])

Current_Coordinate = input(
    "Let's get started! What is the first coordinate you want your patrol boat (2 squares)? "
    "Each coordinate starts with A to J (please use uppercase), then 1 to 10 with no spaces: "
)


converted_coordinate = check_coordinates_answer(Current_Coordinate)


if converted_coordinate:
    print("Coordinate will be added!")
    Patrol_Boat[0] = converted_coordinate

else:
    print("Invalid coordinate!")
