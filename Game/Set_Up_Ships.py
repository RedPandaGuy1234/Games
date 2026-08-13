import Locations

Current_Coordinate = 0

Patrol_Boat = [0, 0]
Battleship = [0, 0, 0, 0]
Destroyer = [0, 0, 0]
Submarine = [0, 0, 0]
Carrier = [0, 0, 0, 0, 0]
is_coordinate_correct = False

col_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def make_sure_coordinate_is_correct(ship, num):
    while not is_coordinate_correct:
        Current_Coordinate = input("Invalid coordinate! Remember; the coordinate must have the first part being a letter from A to J, and the second part being 1 to 10. Please re-enter the coordinate.")
        converted_coordinate = check_coordinates_answer(Current_Coordinate)
        if converted_coordinate:
            print("The coordinate is now correct!")
            ship[num] = converted_coordinate
            is_coordinate_correct = True



def check_coordinates_answer(Coordinate):
    if (isinstance(Coordinate, str) and len(Coordinate) >= 2 
            and Coordinate[0] in col_letters and Coordinate[1:].isdigit()
            and 1 <= int(Coordinate[1:]) <= 10):
        column_number = col_letters.index(Coordinate[0])
        row_number = int(Coordinate[1:])
        return (column_number, row_number)
    else:
        return None

Current_Coordinate = input(
    "Let's get started! What is the first coordinate you want your patrol boat (2 squares)? "
    "Each coordinate starts with A to J (please use uppercase), then 1 to 10 with no spaces: "
)


converted_coordinate = check_coordinates_answer(Current_Coordinate)


if converted_coordinate:
    print("Coordinate will be added!")
    Patrol_Boat[0] = converted_coordinate

else:
    make_sure_coordinate_is_correct(Patrol_Boat, 0)
is_coordinate_correct = False
