def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    add(x, y)
    sub(x, y)
    div(x, y)



def add(a, b):
    sum = (a + b)
    print("Sum: ", sum)  
def sub(a, b):
    difference = round(a - b)
    print("Difference: ", difference)
def div(a, b):
    if b != 0:
        division = round(a / b, 2)
        print("Division: ", division)  
    else:
        print("Error")
        


main()
