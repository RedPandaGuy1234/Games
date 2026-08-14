import Locations

Current_Coordinate = 0

Patrol_Boat = [0, 0]
Battleship = [0, 0, 0, 0]
Destroyer = [0, 0, 0]
Submarine = [0, 0, 0]
Carrier = [0, 0, 0, 0, 0]
Used_Coordinates = [0] * 17

col_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def make_sure_coordinate_is_correct(ship, num, coordinate_num):
    is_coordinate_correct = False
    while not is_coordinate_correct:
        Current_Coordinate = input("Invalid coordinate! Remember; the coordinate must have the first part being a letter from A to J, the second part being 1 to 10, and the letter is uppercase. Please re-enter the coordinate.")
        converted_coordinate = check_coordinates_answer(Current_Coordinate)
        if converted_coordinate:
            print("The coordinate is now correct!")
            ship[num] = converted_coordinate
            Used_Coordinates[coordinate_num] = converted_coordinate
            is_coordinate_correct = True


def check_coordinates_answer(Coordinate, ship=None, is_first_coordinate=True):
    if (isinstance(Coordinate, str) and len(Coordinate) >= 2 
            and Coordinate[0] in col_letters and Coordinate[1:].isdigit()
            and 1 <= int(Coordinate[1:]) <= 10):
        column_number = col_letters.index(Coordinate[0])
        row_number = int(Coordinate[1:])
        new_coordinate = (column_number, row_number)

        for existing in Used_Coordinates:
            if existing != 0 and existing == new_coordinate:
                print("That coordinate is already taken! Please choose another.")
                return None
                
        if not is_first_coordinate and ship is not None:
            first_coordinate = ship[0]
            if first_coordinate != 0:
                same_column = new_coordinate[0] == first_coordinate[0]
                same_row = new_coordinate[1] == first_coordinate[1]
                if not (same_column or same_row):
                    print("That coordinate must share a row or column with the ship's first coordinate!")
                    return None

        return new_coordinate
    else:
        return None

Current_Coordinate = input(
    "Let's get started! What is the first coordinate you want your patrol boat (2 squares)? "
    "Each coordinate starts with A to J (please use uppercase), then 1 to 10 with no spaces: "
)


converted_coordinate = check_coordinates_answer(Current_Coordinate, Patrol_Boat, True)


if converted_coordinate:
    print("Coordinate will be added!")
    Patrol_Boat[0] = converted_coordinate
    Used_Coordinates[0] = converted_coordinate
    print(Patrol_Boat[0])

else:
    make_sure_coordinate_is_correct(Patrol_Boat, 0, 0)

Current_Coordinate = input("Okay, you now know how to do this! Now, let's do this with the other coordinate in the patrol boat. Please enter it.")
converted_coordinate = check_coordinates_answer(Current_Coordinate, Patrol_Boat, True)

if converted_coordinate:
    print("This is another correct coordinate! Let's keep going through the coordinates.")
    Patrol_Boat[1] = converted_coordinate
    Used_Coordinates[1] = converted_coordinate    
else: 
    make_sure_coordinate_is_correct(Patrol_Boat, 1, 1)
    Patrol_Boat[1] = converted_coordinate
    Used_Coordinates[1] = converted_coordinate
