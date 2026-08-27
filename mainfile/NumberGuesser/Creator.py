import random

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
      return Bound
    else:
      print("This was not an integer. Please try again.")

print("Hi!")
Low_Bound = Set_Bounds(Low_Bound, "lower")
High_Bound = Set_Bounds(High_Bound, "higher")
is_low_more = False
while not is_low_more:
  if Low_Bound > High_Bound:
    print("The lower part of the range is greater than the higher one. Please restart.")
    Low_Bound = Set_Bounds(Low_Bound, "lower")
    High_Bound = Set_Bounds(High_Bound, "higher")
  else: 
    is_low_more = True
Number = random.randint(Low_Bound, High_Bound)
#This is a test
print (Number)

