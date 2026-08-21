import random

choices = ["Rock", "Paper", "Scissors"]

# Usage counters and scores
rock_usage = 0
paper_usage = 0
scissors_usage = 0
player_score = 0
bot_score = 0

print("Let's begin! Enter 0 for Rock, 1 for Paper, 2 for Scissors. Type 'q' to quit.")

while True:
    user_input = input("Your choice (0/1/2 or q): ").strip().lower()
    if user_input == "q":
        break

    try:
        person_choice = int(user_input)
    except ValueError:
        print("Invalid input. Please enter 0, 1, 2, or q.")
        continue

    if person_choice not in (0, 1, 2):
        print("Invalid choice. Enter 0, 1, or 2.")
        continue

    # Update usage counters
    if person_choice == 0:
        rock_usage += 1
    elif person_choice == 1:
        paper_usage += 1
    else:
        scissors_usage += 1

    # Bot makes a random choice
    bot_choice = random.randint(0, 2)

    print(f"You chose {choices[person_choice]}; Bot chose {choices[bot_choice]}.")

    # Determine winner: (person - bot) % 3 == 1 => person wins; == 2 => bot wins; == 0 => tie
    result = (person_choice - bot_choice) % 3
    if result == 1:
        player_score += 1
        print("You win this round!")
    elif result == 2:
        bot_score += 1
        print("Bot wins this round!")
    else:
        print("It's a tie!")

    print(f"Score -> You: {player_score}, Bot: {bot_score}\n")

# Final stats
print("Final results:")
print(f"You: {player_score}, Bot: {bot_score}")
print(f"Usage - Rock: {rock_usage}, Paper: {paper_usage}, Scissors: {scissors_usage}")
