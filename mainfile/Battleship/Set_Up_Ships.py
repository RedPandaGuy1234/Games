"""Set up ship placements for a game of Battleship."""

import Locations  # noqa: F401  # pylint: disable=unused-import

col_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

patrol_boat = [0, 0]
battleship_ship = [0, 0, 0, 0]
destroyer = [0, 0, 0]
submarine = [0, 0, 0]
carrier = [0, 0, 0, 0, 0]
used_coordinates = [0] * 17


def check_coordinates_answer(coordinate, ship=None, is_first_coordinate=True):
    """Validate a coordinate string and return a (column, row) tuple, or None."""
    is_valid_format = (
        isinstance(coordinate, str)
        and len(coordinate) >= 2
        and coordinate[0] in col_letters
        and coordinate[1:].isdigit()
        and 1 <= int(coordinate[1:]) <= 10
    )
    if not is_valid_format:
        return None

    column_number = col_letters.index(coordinate[0])
    row_number = int(coordinate[1:])
    new_coordinate = (column_number, row_number)

    for existing in used_coordinates:
        if existing != 0 and existing == new_coordinate:
            print("That coordinate is already taken! Please choose another.")
            return None

    if not is_first_coordinate and ship is not None:
        first_coordinate = ship[0]
        if first_coordinate != 0:
            same_column = new_coordinate[0] == first_coordinate[0]
            same_row = new_coordinate[1] == first_coordinate[1]
            if not (same_column or same_row):
                print(
                    "That coordinate must share a row or column with the "
                    "ship's first coordinate!"
                )
                return None

    return new_coordinate


def make_sure_coordinate_is_correct(ship, num, coordinate_num):
    """Keep prompting until a valid coordinate is entered, then store it."""
    is_coordinate_correct = False
    while not is_coordinate_correct:
        current_coordinate = input(
            "Invalid coordinate! Remember; the coordinate must have the "
            "first part being a letter from A to J, the second part being "
            "1 to 10, and the letter is uppercase. Please re-enter the "
            "coordinate."
        )
        converted_coordinate = check_coordinates_answer(current_coordinate)
        if converted_coordinate:
            print("The coordinate is now correct!")
            ship[num] = converted_coordinate
            used_coordinates[coordinate_num] = converted_coordinate
            is_coordinate_correct = True


current_coordinate = input(
    "Let's get started! What is the first coordinate you want your patrol "
    "boat (2 squares)? Each coordinate starts with A to J (please use "
    "uppercase), then 1 to 10 with no spaces: "
)

converted_coordinate = check_coordinates_answer(current_coordinate, patrol_boat, True)

if converted_coordinate:
    print("Coordinate will be added!")
    patrol_boat[0] = converted_coordinate
    used_coordinates[0] = converted_coordinate
    print(patrol_boat[0])
else:
    make_sure_coordinate_is_correct(patrol_boat, 0, 0)

current_coordinate = input(
    "Okay, you now know how to do this! Now, let's do this with the other "
    "coordinate in the patrol boat. Please enter it."
)
converted_coordinate = check_coordinates_answer(current_coordinate, patrol_boat, True)

if converted_coordinate:
    print(
        "This is another correct coordinate! Let's keep going through the "
        "coordinates."
    )
    patrol_boat[1] = converted_coordinate
    used_coordinates[1] = converted_coordinate
else:
    make_sure_coordinate_is_correct(patrol_boat, 1, 1)
    patrol_boat[1] = converted_coordinate
    used_coordinates[1] = converted_coordinate
