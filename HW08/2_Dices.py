from datetime import datetime
import random
import xlsxwriter

"""
2. Взять код, который писали для игры кубики на лекции 7 https://github.com/VitaliiFisenko95/python_lk/blob/master/lk7/class_work.py#L150 ,
проанализировать его (по возможности улучшить). Результат игры в кубики нужно записать в файл (json, yaml, csv, xlsx) по раундам. 
В данных раунда должно быть:
 - время хода каждого из игроков
 - количество очков за раунд
 - номер игрока (или имя)
"""

"""
Было:
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""

def first_player():
    input('Игрок 1, ваш ход')
    return random.randint(1, 6)


def second_player():
    input('Игрок 2, ваш ход')
    return random.randint(1, 6)


def main():
    start = input('Start game yes|no')

    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Dices.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        worksheet.write(row, 0, 'Round')
        worksheet.write(row, 1, 'Score1')
        worksheet.write(row, 2, 'Time1')
        worksheet.write(row, 3, 'Score2')
        worksheet.write(row, 4, 'Time2')
        counter = 10
        while counter:
            row += 1
            time1 = datetime.now()
            player_1_value = first_player()
            delta = datetime.now() - time1
            sec1 = delta.seconds
            time1 = datetime.now()
            player_2_value = second_player()
            delta = datetime.now() - time1
            sec2 = delta.seconds

            worksheet.write(row, 0, row)
            worksheet.write(row, 1, player_1_value)
            worksheet.write(row, 2, sec1)
            worksheet.write(row, 3, player_2_value)
            worksheet.write(row, 4, sec2)

            if player_1_value != player_2_value:
                player_1_sum += player_1_value
                player_2_sum += player_2_value
            else:
                worksheet.write(row, 5, " We skip this result!")

            counter -= 1

        worksheet.write(row+1, 0, 'Total')
        worksheet.write(row+1, 1, player_1_sum)
        worksheet.write(row+1, 3, player_2_sum)


        if player_1_sum > player_2_sum:
            print('First player won')
            print(player_1_sum)
            print(player_2_sum)
        elif player_1_sum == player_2_sum:
            print('Победила дружба')
            print(player_1_sum)
            print(player_2_sum)
        else:
            print('Second player won')
            print(player_1_sum)
            print(player_2_sum)

        workbook.close()

main()