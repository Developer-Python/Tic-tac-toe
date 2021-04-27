from random import randint


GAME = True
array_win = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]
game_field = []


def check_move():
    return print(f'Заняты ходы: {sorted(game_field)}')


def check_win(winner, array):

    count = 0

    for i in array_win:
        try:
            for pos, c in enumerate(array):

                if i == [ array[pos], array[pos+1],array[pos+2] ]:
                    count+=1

        except IndexError:
            pass

    if count >= 1:
        print(f'Win - {winner}!')
        exit(0)



def check_error(move):

    ERROR = True

    while ERROR:
        if ''.join(map(str, (game_field))).find(str(move)) == -1 and move <= 9:
            return move
        else:
            new_move = int(input('Поле занято, выбирите другое: '))
            return check_error(new_move)



def Al():

    al_move = randint(1,9)

    if ''.join(map(str, (game_field))).find(str(al_move)) == -1:
        return al_move
    else:
        return Al()



while GAME:

    ai_1 = Al()
    game_field.append(ai_1)
    print(f'Искусственный интеллект: {ai_1}')

    check_move()

    human_1 = check_error(int(input('Вы: ')))
    game_field.append(human_1)

    ai_2 = Al()
    game_field.append(ai_2)
    print(f'Искусственный интеллект: {ai_2}')
    check_move()

    human_2 = check_error(int(input('Вы: ')))
    game_field.append(human_2)
    check_move()
    ai_3 = Al()
    game_field.append(ai_3)
    print(f'Искусственный интеллект: {ai_3}')
    check_move()
    human_3 = check_error(int(input('Вы: ')))
    game_field.append(human_3)
    check_move()
    check_win('ai', sorted([ai_1, ai_2, ai_3]))

    check_win('human', sorted([human_1, human_2, human_3]))

    ai_4 = Al()
    game_field.append(ai_4)
    print(f'Искусственный интеллект: {ai_4}')
    check_move()

    check_win('ai', sorted([ai_1, ai_2, ai_3, ai_4]))

    human_4 = check_error(int(input('Вы: ')))
    game_field.append(human_4)


    check_win('human', sorted([human_1, human_2, human_3, human_4]))

    ai_5 = Al()
    game_field.append(ai_5)
    print(f'Искусственный интеллект: {ai_5}')
    check_move()
    check_win('human', sorted([human_1, human_2, human_3, human_4]))

    print('Tied')

    exit(0)
