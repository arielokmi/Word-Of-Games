from random import randint
import requests
def get_money_interval(number,difficulty):
    usa_rate = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    usa_rate = usa_rate['rates']['ILS']
    t = number*usa_rate
    d = difficulty
    interval =  [t - (5 - d), t +(5 - d)]
    return interval

def get_guess_from_user(number):
    input_user = input(f"Enter the value of {number} in USD currenty\n")
    while not input_user.isdigit():
        input_user = input(f"Try again,Enter the value of {number} in USD currenty\n")
    return input_user

def play(difficulty):
    number = randint(1, 100)
    money_intreval = get_money_interval(number,difficulty)
    user_guess = get_guess_from_user(number)
    if int(user_guess) > money_intreval[0] and int(user_guess) < money_intreval[1]:
        return True

