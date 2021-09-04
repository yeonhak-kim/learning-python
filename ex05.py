## Exercise 05: More Variables and Printing

my_name = 'Yeonhak Kim'
my_age = 26
my_height = 180
my_weight = 77
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimetes tall.")
print(f"He's {my_weight} kg heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight 
print(f"If I add {my_age}, {my_height}, and {my_weight} we get {total}.")


# Personal Comment: f -> format: f"string-statement, {variable}, string-statement",
#                 f interprets {variable-name} and brings value of variable-name in the code.