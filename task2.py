#Задача 2: Найдите сумму цифр трехзначного числа.
#Пример: 123 -> 6 (1 + 2 + 3), 100 -> 1 (1 + 0 + 0)

a = str(input('Enter three-digit number: '))

x = int(a[0])
y = int(a[1])
z = int(a[2])
sum = x + y + z
print(f'Summ of the numbers {x} {y} {z} is --> {sum}')