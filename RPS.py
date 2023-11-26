import random
import os
import stdiomask
user_wins = 0
computer_wins = 0
os.system("cls")
options = ["r", "p", "s"]
print("Welcome to the Rock Paper Scissors game!")
playmode=input("Do you want to play against the computer or a friend? (C/F) ").lower()
if playmode == "c":
    print("Try and beat me in the game of Rock Paper Scissors! - the Evil Computer")

    while True:
        user_input = input("Type R/P/S or Q to quit: ").lower()
        if user_input == "q":
            print("You quit the game!")
            print("You won " + str(user_wins) + " times.")
            print("The computer won " + str(computer_wins) + " times.")
            print("Goodbye!")
            break
        if user_input not in options:
            print("Please enter a valid option!")
            continue
        computer_input = random.choice(options)

        print("The computer chose " + computer_input + ".")

        if user_input == "r" and computer_input == "s":
            print("You won!")
            user_wins += 1
            continue
        elif user_input == "p" and computer_input == "r":
            print("You won!")
            user_wins += 1
            continue
        elif user_input == "s" and computer_input == "p":
            print("You won!")
            user_wins += 1
            continue
        elif user_input == computer_input:
            print("It's a tie!")
            continue
        else:
            print("You lost!")
            computer_wins += 1
            continue
elif playmode == "f":
    print("Try and beat your friend in the game of Rock Paper Scissors!")
    while True:
        
        user_input = stdiomask.getpass(prompt="Player 1, type R/P/S or Q to quit: ", mask="").lower()
        if user_input == "q":
            print("You quit the game!")
            print("Player 1 won " + str(user_wins) + " times.")
            print("Player 2 won " + str(computer_wins) + " times.")
            print("Goodbye!")
            break
        if user_input not in options:
            print("Please enter a valid option!")
            continue
        computer_input = stdiomask.getpass(prompt="Player 2, type R/P/S or Q to quit: ", mask="").lower()
        if computer_input == "q":
            print("You quit the game!")
            print("Player 1 won " + str(user_wins) + " times.")
            print("Player 2 won " + str(computer_wins) + " times.")
            print("Goodbye!")
            break
        if computer_input not in options:
            print("Please enter a valid option!")
            continue
        print("Player 1 chose " + user_input + ".")
        print("Player 2 chose " + computer_input + ".")

        if user_input == "r" and computer_input == "s":
            print("Player 1 won!")
            user_wins += 1
            continue
        elif user_input == "p" and computer_input == "r":
            print("Player 1 won!")
            user_wins += 1
            continue
        elif user_input == "s" and computer_input == "p":
            print("Player 1 won!")
            user_wins += 1
            continue
        elif user_input == computer_input:
            print("It's a tie!")
            continue
        else:
            print("Player 2 won!")
            computer_wins += 1
            continue
else:
    print("Please enter a valid option!")
    quit()

