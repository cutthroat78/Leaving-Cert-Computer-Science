# Question 16(a)
# Student number

s_name = input("Enter your surname: ")
f_name = input("Enter your first name: ")
age = int(input("Enter your age: "))
eircode = input("Enter your Eircode: ")

print("Hello", f_name, s_name, "you are", age, "years old")
print("Eircode is", eircode)

if 

if age < 12:
    print(f_name + ", " + "you are too young to get a vaccine")
elif age >= 12 and age <= 49:
    print(f_name + ", " + "you will recieve the MRNA vaccine")
elif age >= 50:
    print(f_name + ", " + "you will recieve the ADENO vaccine")
