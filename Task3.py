# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

number = int(input("Введите трёхзначное число: \n"))
first_digit = number // 100
second_digit = (number % 100) // 10
third_digit = number % 10

sum_of_number = first_digit + second_digit + third_digit
product_of_numbers = first_digit * second_digit * third_digit

print('Сумма цифр =', sum_of_number)
print('Произведение цифр =', product_of_numbers)
