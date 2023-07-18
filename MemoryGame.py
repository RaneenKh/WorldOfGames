import random
import time

def generate_sequence(difficulty):
    rand_list = []
    for i in range(difficulty):
        rand_list.append(random.randint(1, 101))
    return rand_list

def get_list_from_user(difficulty):
    input_list = []
    for i in range(0, difficulty):
        number = int(input("Please enter the numbers that u remember by sequence (one by one)"))
        # adding the element
        input_list.append(number)
    return input_list
def is_list_equal(random_list, input_user_list):
    return random_list == input_user_list



def play(difficulty):
    random_list = generate_sequence(difficulty)
    print(random_list, end='', flush=True)
    time.sleep(0.7)
    print('\r' + ' ' * len(str(random_list)), end='', flush=True)
    input_user_list = get_list_from_user(difficulty)
    game_flag = is_list_equal(random_list, input_user_list)
    if(game_flag):
        print("Wohho! u have guessed all the numbers correctly")
        return True
    else:
        print("Opps!,  u have not guessed all the numbers correctly. Best of luck next time")
        return False


