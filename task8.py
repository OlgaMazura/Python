# Задача 8: Требуется определить, можно ли от шоколадки размером n×m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример: 3 2 4 -> yes, 3 2 1 -> no

n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))
k = int(input('How many pieces do you want? '))

if(k//n or k//m):
    print(f'Yes! You are lucky!')
else:
    print(f'No! Try again!')
