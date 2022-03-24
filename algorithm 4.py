x = int(input("Enter your starting number ")) # Step one, enter an input set as an integer

print(x) # Print the number input

while x < 50:
    x *= 3
    print(x)
    if x % 2 == 0:
        x += 2
        print(x)
        continue
