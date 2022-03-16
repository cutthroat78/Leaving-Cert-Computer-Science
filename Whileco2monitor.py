CO2 = int(input("Please enter the CO2 Reading")) # To Ask for the CO2 Reading
if CO2<539:
    print("Green")
elif CO2>540 and CO2<1238:
    print("Orange")
elif CO2>1239:
    print("Red")

print("Done")
