#100 Days of coding day 12: Number Guessing Game project
import random
import os


print("Welcome to: Number Guessing Game")
play_again = "y"
while play_again == "y":
    os.system('cls')
    num_final = random.randint(1,100)
    difficulty = input("Easy or Hard Mode? e/h: ")
    guesses_remaining = 0
    if difficulty == "e":
        guesses_remaining = 10
    elif difficulty == "h":
        guesses_remaining = 5

    while guesses_remaining > 0:
        print(f"Guesses remaining: {guesses_remaining}")
        guesses_remaining -= 1
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > num_final:
            print("Too High")
        elif guess < num_final:
            print("Too Low")
        elif guess == num_final:
            print("Correct: You Win")
            break;
    if guesses_remaining == 0:
        print("No guesses remaining. You lose.")
    play_again = input("Would you like to play again? y/n ")