import random
random_number = random.randint(1,9)
user_guess = int(input("Guess a number: "))
while random_number != user_guess:
    user_guess =int(input("Try another guess: "))
print("Well guessed")