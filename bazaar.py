
# #Задача на проверку простоты числа
number = int(input('Введите числовое значение: '))
q = 2
res = 0
while q <= number // 2:
   if number % q == 0:
       res += 1
   q += 1
if res <= 0:
   print(True)
else:
   print(False)


#Задача о сортировке массива

mas = [int(y) for y in input('Введите числа: ').split()]
for i in range(0, len(mas)):
    for x in range(0, len(mas) - (i + 1)):
        if mas[x] > mas[x + 1]:
            mas[x], mas[x + 1] = mas[x + 1], mas[x]
print(f'Ответ:  {mas}')





#Задача о поиске наибольшего элемента в массиве

mas = [int(i) for i in input('Введите несколько чисел:  ').split()]
x = mas[0]
i = 1
while i < len(mas):
    if mas[i] > x:
        x = mas[i]
    i += 1
print(f'Максимальное число   {x}')



#Задача о вычислении числа Фибоначчи

fib = int(input('Введите число фибоначи:'))
if fib == 0:
    print(0)
else:
    a = 0
    b = 1
    i = 2
    while i <= fib:
        sum_ab = a + b
        a = b
        b = sum_ab
        i += 1
    print(f'Число Фибоначчи: {b}')

