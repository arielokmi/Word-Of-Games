from random import randint

def generate_number(max_number_difficulty):
    secret_number = randint(0,max_number_difficulty)
    return secret_number
    print(secret_number)

def get_guess_from_user(max_number_difficulty):
    guss_from_user = input(f"choose between 1 - {max_number_difficulty}\n")
    while not guss_from_user.isdigit() or int(guss_from_user) <= 0 or int(guss_from_user) > max_number_difficulty:
        guss_from_user = input(f" Try again, choose between 1 - {max_number_difficulty}\n")
    return guss_from_user

def compare_results(secret_number,guss_from_user):
    if secret_number == guss_from_user:
        return True

def play(difficulty):
    max_number_difficulty = [10, 50, 100, 200, 500]
    max_number_difficulty = max_number_difficulty[difficulty-1]
    compare_results(generate_number(max_number_difficulty), get_guess_from_user(max_number_difficulty))
    return True