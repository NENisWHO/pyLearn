
num_char = len(input("what is your name? "))
#print("your name has" + num_char + "characters")
#error: TypeError: can only concatenate str (not "int") to str
print("type of num_char is ", type(num_char))

new_num_char = str(num_char)
print("your name has " + new_num_char + " characters")

a = float(123)
print(type(a))

print(str(10) + str(100))
print(70 + float(123.54534))