# Hunter C. Sylvester
# Purpose: Create a guessing game with values 1-100 inclusive

# Import modules needed to create this program
# This helps with creating a random number
import random

print("Welcome to the Number Guessing Game! \n1. You will randomly choose a number between 1 and 100 inclusive. \n2. I will let"
      " you know if it is high, low, or correct. \n3. You will have the option to continue or quit. \n")

# Have i set to 0 for counting and compGuess for the random number guessed by the computer
i = 0
compGuess = random.randint(1, 100)

# Create a loop to continue guessing until you get the number correct
while True:
    try:
        # Allows the user the option to quit after the first game or continue
        if i > 0:
            quitGame = str(input('Would you like to continue playing or quit?  To quit press, "q" and [ENTER]. '
                                 'To continue, press any other key and [ENTER]. '))
            if quitGame == "q":
                print("Thank you so much for playing, please come again!!!")
                exit()
            else:
                pass
    except Exception as e:
        print(f"Got an error: {e}\n")

    # Creates a loop to count how many times a player guesses and gives a hint if their value is wrong
    try:
        yourGuess = int(input("Please pick a natural number between 1-100 inclusive: "))
        while yourGuess != compGuess:
            i += 1
            if 100 >= int(yourGuess) >= 1:
                if yourGuess < compGuess:
                    print("Your value is low, pick another number! ")
                elif yourGuess > compGuess:
                    print("Your value is high, pick another number! ")
                break

        # Congratulates the player for guessing the correct guess and gives how many tries
        if yourGuess == compGuess:
            i = i + 1
            print("Congratulations! You guessed the same value that I did! Woo! Woo!  It only took you", i, "tries!"
                  " Not bad!!!")
            break

    except Exception as e:
        print(f"Got an error: {e}\n")