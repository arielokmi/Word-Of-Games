from random import randint
import time
import Utils
def generate_sequence(difficulty):
    list = []
    for i in range(difficulty):
        num = randint(1,101)
        print(num,sep=' ', end=' ', flush=True)
        list.append(num)
    print()
    time.sleep(7)
    Utils.Screen_cleaner()
    return list

def get_list_from_user(difficulty):
    list_from_input = []
    while len(list_from_input) == 0:
        get_list_from_input = input(f'now,you need to put all {difficulty} the numbers that was show.\n')
        list_from_input = get_list_from_input.split()
    for num in list_from_input:
        while  len(list_from_input) == 0 or len(list_from_input) > difficulty or len(list_from_input) < difficulty or list_from_input.count(num) > 1 or  not num.isdigit() or int(num) == 0:
             get_list_from_input = input(f'try again\nnow,you need to put all {difficulty} the numbers that was show\n')
             list_from_input = get_list_from_input.split()
    return list_from_input

def  is_list_equal(list_guess,list_user):
    count = 0
    for check in range(len(list_user)):
        if int(list_user[check]) == int(list_guess[check]):
            count = count+1
    if count == len(list_user):
        print('True')
    else:
        print("False")
def play(difficulty ):
    is_list_equal(generate_sequence(difficulty),get_list_from_user(difficulty))
    return True

