Number = 0
Low_Bound = 0
High_Bound = 0
is_low_more = False
def Set_Bounds(Bound, range): 
  is_Correct = False 
  while not is_Correct:
    Bound = input(f"Please say the {range} part of the range for creating my number!")
    if Bound.isdigit():
      print("Okay!")
      is_Correct = True
    else:
      print("This was not a number. Please try again.")

print("Hi!")
Set_Bounds(Low_Bound, "lower")
Set_Bounds(High_Bound, "higher")
while not is_low_more:
  if Low_Bound > High_Bound:
    print("The lower part of the range is greater than the higher one. Please restart.")
    Set_Bounds(Low_Bound, "lower")
    Set_Bounds(High_Bound, "higher")
  else: 
    is_low_more = True

