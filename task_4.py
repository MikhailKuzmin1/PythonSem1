haigth = int(input('Введите колличество долек в длинну: '))
width = int(input('Введите колличество долек в ширину: '))
chocolate = int(input('Введите колличество долек, которое хотите отломить: '))
S = haigth*width
if chocolate < S  and (chocolate%width == 0 or chocolate%haigth == 0):
    print('Можно')
else:
    print('Нельзя')  