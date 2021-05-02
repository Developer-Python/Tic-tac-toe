

# ---------------------------------------------------------------------------------------------------------------- #


# Модель приложения GUI
from model import Ui_Dialog

# Виджеты
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

# Модуль для рандомных чисел
from random import randint

# Модуль для работы с os, sys
import os, sys


# ---------------------------------------------------------------------------------------------------------------- #


# Создание приложения
app = QtWidgets.QApplication(sys.argv)

# Инициализация форм приложения
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# ---------------------------------------------------------------------------------------------------------------- #


# Все возможные выйграшные позиций
win_pos = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]
# Счётчик всех ходов в игре
count_moves = []
# Ходы сделанные ИИ
ai_moves = []
# Ходы сделанные Человеком
human_moves = []
# Поля
fields = [ui.field_1,ui.field_2,ui.field_3,ui.field_4,ui.field_5,ui.field_6,ui.field_7,ui.field_8,ui.field_9]


# ---------------------------------------------------------------------------------------------------------------- #


def check_win(winner, array):

    """====================================="""
    """      Проверка выйграл ли кто-то     """
    """====================================="""

    # Перебераем все выйгрышные позиции в игре
    for i in win_pos:

        # Попытка сравнить
        try:
            # Перебераем ходы которые были сделаны
            for pos, c in enumerate(sorted(array)):

                # Проверяем если сделанные ходы ровняются выйгрышным, то значит победа
                if (i == [ array[pos], array[pos+1],array[pos+2] ]) or (i == [ array[pos], array[pos+1],array[pos+3] ]) or (i == [ array[pos], array[pos+2],array[pos+3] ]):
                    ui.label_winner.setText(f'Победил: {winner}!')
                    [i.setEnabled(False) for i in fields]

        except IndexError:
            pass



def ai():

    """=================================="""
    """      Искусственный Интеллект     """
    """=================================="""

    # Если общее кол-во ходов 9, завершить игру
    if len(count_moves) == 9:

        # Вывод о том кто выйграл
        ui.label_winner.setText('Ничья!')

        # Дизактивация всех кнопок
        [i.setEnabled(False) for i in fields]

        # Остановка рекурсии
        return 0

    # ИИ выбирает рандомное число
    al_move = randint(1,9)

    # Пойск доступного пустого поля
    if ''.join(map(str, (count_moves))).find(str(al_move)) == -1:
        add_move(ai_moves,count_moves, al_move)
        fields[al_move-1].setText('O')

    else:
        return ai()



def add_move(array1, array2, number_move):

    """======================================"""
    """     Добавиление хода в статистику    """
    """======================================"""
    # Добавление хода в массив
    array1.append(number_move)
    array2.append(number_move)



def human():

    """=================="""
    """       Игрок      """
    """=================="""

    # Проверка на пустое поле для игрока
    if ui.field_1.isChecked() == True and ui.field_1.text() == '':

        # Поставить крестик
        ui.field_1.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 1)

        ui.field_1.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_2.isChecked() == True and ui.field_2.text() == '':

        # Поставить крестик
        ui.field_2.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 2)

        ui.field_2.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_3.isChecked() == True and ui.field_3.text() == '':

        # Поставить крестик
        ui.field_3.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 3)

        ui.field_3.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_4.isChecked() == True and ui.field_4.text() == '':

        # Поставить крестик
        ui.field_4.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 4)

        ui.field_4.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_5.isChecked() == True and ui.field_5.text() == '':

        # Поставить крестик
        ui.field_5.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 5)

        ui.field_5.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_6.isChecked() == True and ui.field_6.text() == '':

        # Поставить крестик
        ui.field_6.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 6)

        ui.field_6.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_7.isChecked() == True and ui.field_7.text() == '':

        # Поставить крестик
        ui.field_7.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 7)

        ui.field_7.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_8.isChecked() == True and ui.field_8.text() == '':

        # Поставить крестик
        ui.field_8.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 8)

        ui.field_8.setChecked(False)

    # Проверка на пустое поле для игрока
    elif ui.field_9.isChecked() == True and ui.field_9.text() == '':

        # Поставить крестик
        ui.field_9.setText('X')

        # Добавить этот ход в статистику
        add_move(human_moves, count_moves, 9)

        ui.field_9.setChecked(False)




def start_game():

    """=================="""
    """       Игра      """
    """=================="""

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 0:
        # Ход игрока
        human()

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 1:
        # Ход ИИ
        ai()

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 2:

        # Ход игрока
        human()

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 3:

        # Ход ИИ
        ai()

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 4:

        # Ход игрока
        human()

        # Проверка кто выйграл после хода
        check_win('Игрок', sorted(human_moves))

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 5:

        # Ход ИИ
        ai()

        # Проверка кто выйграл после хода
        check_win('ИИ', sorted(ai_moves))

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 6:

        # Ход игрока
        human()

        # Проверка кто выйграл после хода
        check_win('Игрок', sorted(human_moves))

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 7:

        # Ход ИИ
        ai()

        # Проверка кто выйграл после хода
        check_win('ИИ', sorted(ai_moves))

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 8:

        # Ход игрока
        human()

        # Проверка кто выйграл после хода
        check_win('Игрок', sorted(human_moves))

    # Проверка какой сейчас по счёту ход
    if len(count_moves) == 9:
        # Ход ИИ
        ai()

        # Проверка кто выйграл после хода
        check_win('ИИ', sorted(ai_moves))




def restart():

    """=========================="""
    """      Перезапуск игры     """
    """=========================="""

    # Запуск новой игры
    os.startfile(f'{os.getcwd()}\\tic-tac-toe.exe')

    # Закрытие старой игры
    sys.exit(app.exec_())




def exit_app(self):

    """=========================="""
    """       Выход из игры      """
    """=========================="""

    # Закрытие игры
    sys.exit(app.exec_())


# ---------------------------------------------------------------------------------------------------------------- #


# Отслеживание события нажатия на кнопки
ui.field_1.clicked.connect(start_game)
ui.field_2.clicked.connect(start_game)
ui.field_3.clicked.connect(start_game)
ui.field_4.clicked.connect(start_game)
ui.field_5.clicked.connect(start_game)
ui.field_6.clicked.connect(start_game)
ui.field_7.clicked.connect(start_game)
ui.field_8.clicked.connect(start_game)
ui.field_9.clicked.connect(start_game)
ui.pushButton_cancel.clicked.connect(exit_app)
ui.pushButton_restart.clicked.connect(restart)


# ---------------------------------------------------------------------------------------------------------------- #


# Запуск
sys.exit(app.exec_())
