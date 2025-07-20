import random
from colorama import Fore, init


# Initialize colorama
init(autoreset=True)


BANNER = '''
 #####    ##   ##### ##### #      ######  ####  #    # # #####   ####     
 #    #  #  #    #     #   #      #      #      #    # # #    # #         
 #####  #    #   #     #   #      #####   ####  ###### # #    #  ####     
 #    # ######   #     #   #      #           # #    # # #####       #    
 #    # #    #   #     #   #      #      #    # #    # # #      #    #    
 #####  #    #   #     #   ###### ######  ####  #    # # #       ####      
'''


def draw_field(field):
    """
    Draw the game board using the provided 2D list.
    """
    for row in field:
        for cell in row:
            if cell == '@':
                print(Fore.GREEN + cell, end=' ')
            elif cell == 'X':
                print(Fore.RED + cell, end=' ')
            elif cell == '-':
                print(Fore.WHITE + cell, end=' ')
            elif cell == '£':
                print(Fore.BLUE + cell, end=' ')
            elif cell == '$':
                print(Fore.YELLOW + cell, end=' ')
            else:
                print(Fore.CYAN + cell, end=' ')
        print()
    print()


def place_ships(board, symbol):
    """
    Randomly place 4 ships on the given board.
    Ships are marked using the provided symbol.
    """
    ships = set()
    while len(ships) < 4:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if (row, col) not in ships:
            ships.add((row, col))
            board[row][col] = symbol


def get_valid_name():
    """
    Prompt the user for a name containing only letters.
    """
    while True:
        name = input(Fore.GREEN + 'Enter your name: ')
        if name.isalpha():
            return name
        print(Fore.RED + 'Name must contain only letters. Please try again.')


def get_valid_guess(guessed):
    """
    Prompt for a row and column guess, ensure integers 0-4 and not guessed before.
    """
    while True:
        try:
            row = int(input('Guess a row (0-4): '))
            col = int(input('Guess a column (0-4): '))
            if not (0 <= row <= 4 and 0 <= col <= 4):
                raise ValueError
            if (row, col) in guessed:
                print(Fore.RED + 'You\'ve already guessed that location. Choose another.')
                continue
            return row, col
        except ValueError:
            print(Fore.RED + 'Invalid input. Enter numbers between 0 and 4.')


def run_game():
    print('*' * 75)
    print(BANNER)
    print('Welcome to Ultimate BATTLESHIPS!')
    print('Board size: 5x5, Ships per side: 4, Turns: 5')
    print('*' * 75)

    name = get_valid_name()
    player_score = 0
    computer_score = 0

    player_board = [['-' for _ in range(5)] for _ in range(5)]
    computer_board = [['-' for _ in range(5)] for _ in range(5)]
    display_board = [['-' for _ in range(5)] for _ in range(5)]

    place_ships(player_board, '@')
    place_ships(computer_board, "'")

    print(f"\n{name}'s Board:")
    draw_field(player_board)

    print("Computer's Board:")
    draw_field(display_board)

    player_guesses = set()
    computer_guesses = set()
    turns = 0

    while turns < 5 and player_score < 4 and computer_score < 4:
        row, col = get_valid_guess(player_guesses)
        player_guesses.add((row, col))
        turns += 1

        if computer_board[row][col] == "'":
            print(Fore.YELLOW + 'Hit! You sank an enemy ship!')
            display_board[row][col] = '$'
            player_score += 1
        else:
            print(Fore.RED + 'Miss!')
            display_board[row][col] = 'X'

        draw_field(display_board)

        while True:
            r = random.randint(0, 4)
            c = random.randint(0, 4)
            if (r, c) not in computer_guesses:
                computer_guesses.add((r, c))
                break
        print(f"Computer guesses: {(r, c)}")
        if player_board[r][c] == '@':
            print(Fore.BLUE + 'Computer hit your ship!')
            player_board[r][c] = '£'
            computer_score += 1
        else:
            print(Fore.WHITE + 'Computer missed.')

        draw_field(player_board)
        print(Fore.CYAN + f"Score -> {name}: {player_score} | Computer: {computer_score}")
        print('-' * 50)

    if player_score > computer_score:
        print(Fore.GREEN + f"Congratulations {name}, you won!")
    elif player_score < computer_score:
        print(Fore.RED + f"Sorry {name}, you lost.")
    else:
        print(Fore.YELLOW + "It's a draw!")


def main():
    while True:
        run_game()
        replay = input(Fore.CYAN + 'Play again? (Y/N): ').strip().lower()
        if replay != 'y':
            print(Fore.MAGENTA + 'Thanks for playing Ultimate BATTLESHIPS!')
            break


if __name__ == '__main__':
    main()
