length_str = input('Pick a length for a rectangle: ', )
width_str = input('Pick a width for a rectangle: ', )

length = float(length_str)
width = float(width_str)

perimeter = (width + length) * 2
area = width * length

perimeter_placeholder = f"{perimeter:2.2f}"
str_perimeter = str(perimeter_placeholder)

area_placeholder = f"{area:2.2f}"
str_area = str(area_placeholder)

print("The perimeter is " + str_perimeter + " and the area is " + str_area)
