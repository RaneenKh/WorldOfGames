import random

secret_number = 0

def generate_number(difficulty):
    secret_number = random.randint(1,difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess_from_user = int(input(f'Please select your guessing number from 1 to {difficulty}: '))
            if guess_from_user in range(1, 6):
                break
            else:
                print("That's not a valid number guess!")
        except:
            print("That's not a valid number guess!")
    return guess_from_user

def compare_results(guess_from_user):
    if secret_number == guess_from_user:
        print("Congrats you have guessed the right number")
        return True
    else:
        print("Opps! you have guessed the wrong number! Best of luck in next time")
        return False

def play(difficulty):
    generate_number(difficulty)
    guess_number_from_user = get_guess_from_user(difficulty)
    compare_results(guess_number_from_user)