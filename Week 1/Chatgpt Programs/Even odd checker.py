def main():
    x = is_valid_int()
    if x is not "Nill":
        if is_even(x):
            print(f'{x} is an even number')
        else:
            print(f'{x} is an odd number')
    
def is_even(n):
    return n % 2 == 0


#Chatgpt Help Function:
def is_valid_int():
    try:
        n = int(input("Enter a number: "))
        return n
    except ValueError:
        print("Enter a valid integer")
        return "Nill"

main()

