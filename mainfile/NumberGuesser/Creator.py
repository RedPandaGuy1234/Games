import random

Number = 0
guess_result = 0
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
      return int(Bound)
    else:
      print("This was not an integer. Please try again.")

def guess_number(Number, guessamount):
  correct = False
  guessamount = guessamount + 1
  guessresult = "start"
  Guess = 0
  while not correct:
    Guess = input("Please tell me your guess!")
    if Guess.isdigit():
      if Guess = Number:
        guessresult = "Correct"
        return guessresult, guessamount
      elif Guess > Number:
        guessresult = "High"
        return guessresult, guessamount
      elif Guess < Number:
        guessresult = "low"
        return guessresult, guessamount
        

print("Hi!")
Low_Bound = Set_Bounds(Low_Bound, "lower")
High_Bound = Set_Bounds(High_Bound, "higher")
is_low_more = False
while not is_low_more:
  if Low_Bound >= High_Bound:
    print("The lower part of the range is greater or equal to the higher one. Please restart.")
    Low_Bound = Set_Bounds(Low_Bound, "lower")
    High_Bound = Set_Bounds(High_Bound, "higher")
  else: 
    is_low_more = True
    
Number = random.randint(Low_Bound, High_Bound)
print(f"I picked a number between {Low_Bound} and {High_Bound}.")
guess_result = guess_number(Number)
