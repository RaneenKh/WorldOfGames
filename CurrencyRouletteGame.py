import requests , random

def get_currency_rate(from_currency, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return rate

def get_money_interval(difficulty):
    currency_rate = get_currency_rate('USD', 'ILS')
    dollars = random.randint(1,100)
    dollars_to_shekels = dollars * currency_rate
    user_guess = get_guess_from_user(dollars)
    difference = abs(dollars_to_shekels - user_guess)
    if difference <= difficulty:
        print("Congrats! you have guessed the convert amount correctly.")
        return True
    else:
        print("Sorry,  you have not guessed the convert amount correctly. Best of luck next time")
        return False

def get_guess_from_user(value):
    return float(input(f'Please enter your guess of {value} Dollars in israeli shekels: '))

def play(difficulty):
    return get_money_interval(difficulty)