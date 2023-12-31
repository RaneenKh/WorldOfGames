import MemoryGame, GuessGame, CurrencyRouletteGame, Score, Utils
import os
def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG). \n' \
           f'Here you can find many cool games to play.'


def load_game():
    while True:
        try:
            print('Please choose a game to play: \n'
                  '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n'
                  '2. Guess Game - guess a number and see if you chose like the computer \n'
                  '3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
            game_chosen = int(input("Please select the game number you would like to play:"))
            if game_chosen in range(1, 4):
                break
            else:
                print("That's not a valid game number option!")
        except:
            print("That's not a valid game number option!")

    while True:
        try:
            game_difficulty = int(input("Please choose game difficulty from 1 to 5:"))
            if game_difficulty in range(1, 6):
                break
            else:
                print("That's not a valid game difficulty option!")
        except:
            print("That's not a valid game difficulty option!")
    if game_chosen == 1:
        win = GuessGame.play(game_difficulty)
        if (win):
            Score.add_score(game_difficulty)
    elif game_chosen == 2:
        win = MemoryGame.play(game_difficulty)
        if (win):
            Score.add_score(game_difficulty)
    else:
        win = CurrencyRouletteGame.play(game_difficulty)
        if (win):
            Score.add_score(game_difficulty)
    play_another_game = input("Would u like to play another game? please write Y for yes and N for no")
    if(play_another_game == 'Y'):
        load_game()

