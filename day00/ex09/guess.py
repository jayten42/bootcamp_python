import random

if __name__ == '__main__':
    secret = random.randint(1, 99)
    count = 0
    print("This is an interactive guessing game!\n"
          "You have to enter a number between 1 and 99 to find out the secret number.\n"
          "Type'exit'to end the game.\n"
          "Good luck!\n")
    while True:
        count += 1
        guess = input("What's your guess between 1 and 99?\n"
                      ">> ")
        if guess == 'exit':
            quit("Goodbye!")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number.")
            continue
        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            if secret == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if count > 1:
                quit("Congratulations, you've got it!\n"
                     "You won in {} attempts!".format(count))
            else:
                quit("Congratulations! You got it on your first try!")


