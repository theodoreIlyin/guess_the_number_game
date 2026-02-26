# import random

# number = random.randint(1,10)
# guess = 0 

# print('Я загадал число от 1 до 10!')

# while guess != number:
#     guess = int(input('Угадай число:'))

#     if guess < number:
#         print('больше')
#     elif guess > number:
#         print('меньше')
#     else:
#         print('ты угадал')

import random 

def generate_number():
    return random.randint(1, 10)

def get_user_guess():
    while True:
        user_input = input('Угадай число: ')
        try:
            return int(user_input)
        except ValueError:
            print('ОШИБКА! Это не число! Попробуй снова.')

def check_guess(guess, number, attempts):
    attempts += 1 

    if guess < number:
        print('Больше')
        return False, attempts
    elif guess > number:
        print('Меньше')
        return False, attempts
    else:
        print('ТЫ УГАДАЛ за', attempts, 'попыток!')
        return True, attempts

def play_game(stats):
    number = generate_number()
    attempts = 0
    
    print('\n' + '='*40)
    print('Я загадал число от 1 до 10')

    while True:
        guess = get_user_guess()
        result, attempts = check_guess(guess, number, attempts)
        
        if result:
            stats['wins'] += 1
            break

    return stats 

def show_stats(stats):
    total_games = stats['wins'] + stats['losses']

    print("\n" + "="*40)
    print("СТАТИСТИКА ИГР:")
    print("Победы от игрока:", stats['wins'])
    print("Сколько игрок проиграл :", stats['losses'])
    print("Всего игр:", total_games)

    if total_games > 0:
        procent = (stats['wins'] * 100) / total_games
        print("Насколько  игрок был прав :", procent)
    else:
        print("Насколько  игрок был прав: 0")

    print("="*40)

def main():
    stats = {
        'wins': 0,
        'losses': 0
    }
    
    print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'УГАДАЙ ЧИСЛО'!")
    
    while True:
        stats = play_game(stats)
        show_stats(stats)

main()
