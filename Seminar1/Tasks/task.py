#Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

print('Введите трехзначное число: ')

number = int(input())

if number > 99 and number < 1000:
    a = number % 10
    b = number % 100 // 10
    c = number // 100
    sum = a + b + c
else: print('Попробуйте еще раз')

print('Сумма цифр в числе: ', sum)





