# Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average
# of the numbers.

print("Choose 3 integers:")
integer_1_str = input('1: ')
integer_2_str = input('2: ')
integer_3_str = input('3: ')

integer_1 = float(integer_1_str)
integer_2 = float(integer_2_str)
integer_3 = float(integer_3_str)

Adding = integer_1 + integer_2 + integer_3
Adding_placeholder = f"{Adding:2.2f}"
Adding_str = str(Adding_placeholder)

print("The sum of the 3 integers is " + Adding_str)

Product = integer_1 * integer_2 * integer_3
Product_placeholder = f"{Product:2.2f}"
Product_str = str(Product_placeholder)

print("The product of the 3 integers is " + Product_str)

Average = (integer_1 + integer_2 + integer_3) / 3
Average_placeholder = f"{Average:2.2f}"
Average_str = str(Average_placeholder)

print("The average of the 3 integers is " + Average_str)
