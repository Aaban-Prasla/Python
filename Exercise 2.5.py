print("Enter a mass in 3 medieval unit: Talents, Pounds and Lots. Eg. a mass of 3 Talents 4 Pounds and 30 Lots.")

Talents_str = input('Talents: ')
Pounds_str = input('Pounds: ')
Lots_str = input('Lots: ')

Talents = float(Talents_str)
Pounds = float(Pounds_str)
Lots = float(Lots_str)

Total_Grams = (Talents * 20 * 32 * 13.3) + (Pounds * 32 * 13.3) + (Lots * 13.3)

Kilograms = Total_Grams / 1000
float(Kilograms)

Int_Kilogram = int(Kilograms)
Leftover_Grams = (Kilograms - Int_Kilogram) * 1000

# Int_Leftover_grams = int(Leftover_Grams)

Deci = f"{Leftover_Grams:3.2f}"

str_kilograms = str(Int_Kilogram)
str_grams = str(Deci)

print("The weight in modern units:")
print(str_kilograms + " kilograms and " + str_grams + " grams.")
