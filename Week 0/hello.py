#Ask user for their name and greet them
name = input("What is your full name? ")

#Remove white spaces

first, middle = name.strip().title().split(" ")


#fstring or special formatting
print(f"Hello, {first}")


#PRINTS
"""
print("Hello,",name)
print("Hello, "+ name)

#use of seperator and end
print("Hello,",name, sep=" ")

print("Hello,", end=" ")
print(name)
"""

#Split the name into parts
"""
if len(parts) == 1:
    print(f"Hello, {parts[0]}")
elif len(parts) == 2:
    print(f"Hello, {parts[0]}")
elif len(parts) == 3:
    print(f"Hello, {parts[1]}")
else:
    print("Hello!")
"""