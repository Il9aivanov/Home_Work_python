print('Введите номер дня недели: ')
a = int(input())
if a > 0 and a < 6:
    print ('Это будний день')
elif a >= 6 and a < 8:
    print('Это выходной день')
else:
    print('Это не день недели')