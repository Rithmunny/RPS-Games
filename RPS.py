import random

def game():
    print("Welcome to RPS Game \n Press 1 for rock \n Press 2 for paper \n Press 3 for scissors")
    guess = int(input("Enter the sign: "))
    x = random.randint(1,3)
    if x == guess:
        print("draw")
    elif x == 1 and guess ==2:
        print("You win")
    elif x == 1 and guess == 3:
        print("You lose")
    elif x == 2 and guess ==3:
        print("You win")
    elif x == 2 and guess == 1:
        print("You lose")
    elif x == 3 and guess ==1:
        print("You win")
    elif x == 3 and guess == 3:
        print("You lose")
game()