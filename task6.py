ы  # Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# подзадачи: ввод номера билета, проверка, вывод билет ок/неок

# через строки с проверкой размера числа
numberTicket = input("Введите номер вашего билета: ")
if len(numberTicket) == 6:
    sumLeft = int(numberTicket[0]) + \
        int(numberTicket[1]) + int(numberTicket[2])
    sumRight = int(numberTicket[3]) + \
        int(numberTicket[4]) + int(numberTicket[5])
    if sumLeft == sumRight:
        print("У вас счастливый билет!")
    else:
        print("Сегодня не ваш день, может в другой раз повезет...")
else:
    print("Вы ввели не шестизначное число, попробуйте ещё раз.")

# через числа с проверкой размера числа
ticketNumber = int(input("Введите номер вашего билета: "))
if 100000 < ticketNumber < 1000000:
    sumLeft = ticketNumber // 100000 % 10 + \
        ticketNumber // 10000 % 10 + ticketNumber // 1000 % 10
    sumRight = ticketNumber // 100 % 10 + ticketNumber // 10 % 10 + ticketNumber % 10
    if sumLeft == sumRight:
        print("У вас счастливый билет!")
    else:
        print("Сегодня не ваш день, может в другой раз повезет...")
else:
    print("Вы ввели не шестизначное число, попробуйте ещё раз.")

# длина номера билета не известна заранее
numTicket = input("Введите номер билета: ")
summaLeft = 0
summaRight = 0
for i in range(len(numTicket)):
    if i < len(numTicket) // 2:
        summaLeft += int(numTicket[i])
    else:
        summaRight += int(numTicket[i])
if summaLeft == summaRight:
    print("У вас счастливый билет!")
else:
    print("Сегодня не ваш день, может в другой раз повезет...")
