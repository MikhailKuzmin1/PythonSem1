number = input('Введите трехначное число: ')
if len(number) == 3:
    res = int(number[0]) + int(number[1]) + int(number[2])
    print(res)
else:
    print("Вы ввели не трехзначное число.")
