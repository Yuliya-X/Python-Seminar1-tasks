# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# подзадачи: ввод строк, ввод столбцов, ввод частей, проверка, вывод ок/неок

row = int(input("Сколько долек шоколада по горизонтали? - "))
col = int(input("Сколько долек шоколада по вертикали? - "))
piece = int(input("Сколько долек шоколада нужно отломить? - "))

chocolateBar = row * col
# не учла разлом по вертикали!!!!!!!!!
# if (piece % 2 == 0) and (piece < chocolateBar):
#     print("yes")
# elif piece < chocolateBar and (row == 1 or col == 1):
#     print("yes")
# else:
#     print("no")

if (piece < chocolateBar) and ((piece % row == 0) or (piece % col == 0)):
    print("yes")
else:
    print("no")
