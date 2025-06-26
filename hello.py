#Ask user for their name and greet them
name = input("What is your name? ")

#Remove white spaces

name = name.strip().title()


#fstring or special formatting
print(f"Hello, {name}")


#PRINTS
"""
print("Hello,",name)
print("Hello, "+ name)

#use of seperator and end
print("Hello,",name, sep=" ")

print("Hello,", end=" ")
print(name)
"""
