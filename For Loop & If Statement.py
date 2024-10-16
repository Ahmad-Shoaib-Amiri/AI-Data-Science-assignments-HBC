'''Multiplication Table'''
while True:
    x = int(input('Enter the number you want to multiply:_ '))
    if x > 1000:
        print('To big number! I can\'t calculate.')
        break
    for i in range(1):
        for j in range(1,11):
            print(x, '*', j, '=', x*j)
