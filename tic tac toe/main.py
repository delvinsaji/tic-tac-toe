def select_symbol():
    final_list = []
    test_1 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    test_2 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    symbol = input('Player1, select your symbol: ')
    while symbol not in ['X', 'O']:
        symbol = input('Invalid input!! Please select your symbol: ')
    else:
        if symbol == 'X':
            for items in test_1:
                final_list.append(items)
            return final_list
        else:
            for items in test_2:
                final_list.append(items)
            return final_list


def ready_start():
    select = input('Are you ready to start the game(Y or N): ')
    while select not in ['Y', "N"]:
        select = input('Invalid input!! Try Again: ')
    else:
        if select == 'Y':
            return select_symbol()
        elif select=='N':
            print('End of the game!!')




final_list = []
for items in ready_start():
    final_list.append(items)


def to_print_board():
    list = ['', '', '', '', '', '', '', '', '', '']
    i = 0
    while i < 9:

        index_input = input('Player: ')
        list[int(index_input)] = final_list[i]

        print('   |     |   ')
        print(f' {list[1]}  | {list[2]}    | {list[3]}  ')
        print('   |     |   ')
        print('--------------')
        print('   |     |   ')
        print(f' {list[4]}  | {list[5]}    | {list[6]}  ')
        print('   |     |   ')
        print('--------------')
        print('   |     |   ')
        print(f' {list[7]}  | {list[8]}    | {list[9]}  ')
        print('   |     |   ')
        i = int(i) + 1
        if list[1] == 'X' and list[2] == 'X' and list[3] == 'X':
            print('X have won the game')
            break
        elif list[1] == 'O' and list[2] == 'O' and list[3] == 'O':
            print('O have won the game')
            break
        elif list[4] == 'X' and list[5] == 'X' and list[6] == 'X':
            print('X have won the game')
            break
        elif list[4] == 'O' and list[5] == 'O' and list[6] == 'O':
            print('O have won the game')
            break
        elif list[7] == 'X' and list[8] == 'X' and list[9] == 'X':
            print('X have won the game')
            break
        elif list[7] == 'O' and list[8] == 'O' and list[9] == 'O':
            print('O have won the game')
            break
        elif list[1] == 'X' and list[4] == 'X' and list[7] == 'X':
            print('X have won the game')
            break
        elif list[1] == 'O' and list[4] == 'O' and list[7] == 'O':
            print('O have won the game')
            break
        elif list[2] == 'X' and list[5] == 'X' and list[8] == 'X':
            print('X have won the game')
            break
        elif list[2] == 'O' and list[5] == 'O' and list[8] == 'O':
            print('O have won the game')
            break
        elif list[3] == 'X' and list[6] == 'X' and list[9] == 'X':
            print('X have won the game')
            break
        elif list[3] == 'O' and list[6] == 'O' and list[9] == 'O':
            print('O have won the game')
            break
        elif list[1] == 'X' and list[5] == 'X' and list[9] == 'X':
            print('X have won the game')
            break
        elif list[3] == 'X' and list[5] == 'X' and list[7] == 'X':
            print('X have won the game')
            break
        elif list[1] == 'O' and list[5] == 'O' and list[9] == 'O':
            print('O have won the game')
            break
        elif list[3] == 'O' and list[5] == 'O' and list[7] == 'O':
            print('O have won the game')
            break
        else:
            pass


def play_again():
    should_play = input('Do you want to play again: ')
    if should_play == 'Y':
        to_print_board()
    elif should_play == 'N':
        print('End of the game! Have a nice day ahead.')
    else:
        print('Invalid input!!')

to_print_board()
play_again()
