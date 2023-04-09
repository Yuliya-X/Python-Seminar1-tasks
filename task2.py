# Задача 2: Найдите сумму цифр трехзначного числа.
# подзадачи: ввод числа, сумма, вывод суммы

number = int(input("Ведите трехзначное чило: "))
sum = 0
while number > 0:
    x = number % 10
    sum += x
    number = number // 10
print(sum)
