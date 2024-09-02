import random

def generate_number():
    return random.randint(100, 999)

def check_number(input, target):
    if int(input) == target:
        return 'Winner'
    
    Pico = False
    for i in range(3):
        if input[i] == str(target)[i]:
            return 'Fermi'
        
        if input[i] in str(target):
            Pico = True

    if (Pico):
        return 'Pico'
    else:
        return 'Bagels'

# start game

print("""Bagels, a deductive logic game.
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")

target = generate_number()
guesses = 0

while guesses < 10:
    user_input = input(f"You have {10 - guesses} guesses left, enter a 3 digit number: ")
    result = check_number(user_input, target)

    print(result)
    guesses += 1

    if result is 'Winner':
        print("You got it!")
        guesses = 11

print(f"The answer is {target}!")