number_ticket = input('Введите номер билета: ')
first_number = number_ticket[:3]
second_number = number_ticket[3:]
sum_first = int(first_number[0]) +  int(first_number[1]) + int(first_number[2])
sum_second = int(second_number[0]) + int(second_number[1]) + int(second_number[2])
if sum_first == sum_second:
    print(f'Билет с номером {number_ticket} - счастливый!')
else:
    print(f'Билет с номером {number_ticket} - не счастливый :(')