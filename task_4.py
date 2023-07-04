length = int(input('Введите колличество долек в длинну: '))
width = int(input('Введите колличество долек в ширину: '))
chocolate = int(input('Введите колличество долек, которое хотите отломить: '))
S = length*width
if chocolate < S  and (chocolate%width == 0 or chocolate%length == 0):
    print('Можно')
else:
    print('Нельзя')  