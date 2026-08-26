Number = 0
Low_Bound = 0
High_Bound = 0
def Set_Bounds(Bound, range): 
  is_Correct = False 
  while not is_Correct:
    Bound = input("Hi! Please say the (range) part of the range for creating my number!")
    if Bound.isdigit():
      print("That is correct!")
      is_Correct = True
    else:
      print("Please try again")

Set_Bounds(Low_Bound, lower)

