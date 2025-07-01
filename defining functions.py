"""
def hello(to="World"):
    print("Hello,", to)

name = input("What is your full name? ")
hello(name)
"""
# Function to greet the user with a default name
# This function takes an optional parameter 'to' with a default value of "World"            
def hello(to="World"):
    print("Hello,", to)


# Function to greet the user
def main():
    name = input("What is your full name? ")
    name = name.strip().title()  # Remove leading/trailing whitespace and capitalize
    hello(name)


# This function is called when the script is run directly
main()