# МОРСКОЙ БОЙ
import random
from random import randint

# Создаем мое поле
matrix_human = [[i for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        matrix_human[i][j] = 0
# Расставим свои карабли куда нравится, в моем случе - на главную диагональ
matrix_human[0][0] = 1
matrix_human[1][1] = 1
matrix_human[2][2] = 1
matrix_human[3][3] = 1
matrix_human[4][4] = 1
matrix_human[5][5] = 1
matrix_human[6][6] = 1
matrix_human[7][7] = 1
matrix_human[8][8] = 1
matrix_human[9][9] = 1

# Создаем поле компьютера, заполненное нулями
matrix_cpu = [[i for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        matrix_cpu[i][j] = 0
# Заполняем поле компьютера 10 кораблями
index = 0
while index < 10:
    x = int(randint(0, 9))
    y = int(randint(0, 9))
    if matrix_cpu[x][y] == 1:
        index -= 1
    else:
        matrix_cpu[x - 1][y - 1] = 1
    index += 1

# СТРЕЛЯЕМ (делаем по 10 выстрелов)
my_result = 0
cpu_result = 0
for i in range(10):
    x = int(input("Введите координату x = ")) # от 1 до 10
    y = int(input("Введите координату y = ")) # от 1 до 10
    if matrix_cpu[x - 1][y - 1] == 1:
        print("Я ПОПАЛ")
        matrix_cpu[x - 1][y - 1] = 0
        my_result += 1
    else:
        print("Я ВЫСТРЕЛИЛ МИМО")

# СТРЕЛЯЕТ КОМПЬЮТЕР
    x = int(randint(0, 9))
    y = int(randint(0, 9))
    if matrix_human[x][y] == 1:
        print("КОМПЬЮТЕР ПОПАЛ")
        matrix_human[x][y] = 0
        cpu_result += 1
    else:
        print("КОМПЬЮТЕР ВЫСТРЕЛИЛ МИМО")

if my_result > cpu_result:
    print(f"Я сбил кораблей: {my_result}, компьютер сбил кораблей: {cpu_result}. ПОБЕДА!!!")
if my_result == cpu_result:
    print(f"Я сбил кораблей: {my_result}, компьютер сбил кораблей: {cpu_result}. НИЧЬЯ!!!")
if my_result < cpu_result:
    print(f"Я сбил кораблей: {my_result}, компьютер сбил кораблей: {cpu_result}. ПОРАЖЕНИЕ!!!")

# МОЖНО ПОТОМ ПОСМОТРЕТЬ НАШИ ПОЛЯ, С УЧЕТОМ СБИТЫХ КОРАБЛЕЙ

# print("МОЕ ПОЛЕ")
# for i in range(len(matrix_human)):
#     for j in range(len(matrix_human)):
#         print(matrix_human[i][j], end=' ')
#     print()
# print("ПОЛЕ КОМПЬЮТЕРА")
# for i in range(len(matrix_cpu)):
#     for j in range(len(matrix_cpu)):
#         print(matrix_cpu[i][j], end=' ')
#     print()