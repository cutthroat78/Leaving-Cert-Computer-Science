#this is very current (;

#save the file as your own name......so Aine_VaccineProgram.py

s_name = input("Enter your surname:")

f_name = input("Enter your first name:")

age = int(input("Enter your age:"))

eircode = input("Enter you Eircode:")

print("Hello", f_name, s_name, "you are", age, "years old and your Eircode is", eircode)

if 12 < age and 49 > age:
    print(f_name + ", you will receive the MRNA vaccine")
elif age > 50:
    print(f_name + ", you will receive the ADENO vaccine")
