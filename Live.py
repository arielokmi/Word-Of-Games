import GuessGame
import CurrencyRouletteGame
import MemoryGame
import Score
from Score import add_score

def welcome(name):
    print(F"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

def load_game():
    list_of_games = [MemoryGame, GuessGame, CurrencyRouletteGame]
     ## game mode section ##
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3.Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    input_game_mode =   input("choose between 1-3.\n")
    input_game_difficulty = input('Please choose game difficulty from 1 to 5:\n')
    while not input_game_mode.isdigit() or not input_game_difficulty.isdigit() or int(input_game_mode) <=  0 or int(input_game_difficulty)  <= 0  or int(input_game_mode) > 3 or int(input_game_difficulty) > 5:
        input_game_mode = input("Try again, choose between 1-3.\n")
        input_game_difficulty = input('Try again, Please choose game difficulty from 1 to 5:\n')
    list_of_games =list_of_games[int(input_game_mode) - 1]
    if list_of_games.play(int(input_game_difficulty)) == True:
        Score.add_score(input_game_difficulty)




