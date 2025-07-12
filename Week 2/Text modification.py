def main():
    while True:
        stri = input("Type: ").strip() or ""

        if not stri:
            print("_______________________________________\n")
            print("No mofiications can be applied to empty input!")
            print("_______________________________________\n")
            continue
        else:
            break

    while True:
        print("\n1. All lowercase",
            "\n2. All uppercase", 
            "\n3. First letter capitalized",
            "\n4. First letter of each word capitalize",
            "\n5. Remove extra whitespaces in input",
            "\n6. Quit program")
    
        print("_______________________________________\n")
    
        get_input = menu()

        if get_input == 6:
            break
        else:
            stri = func(get_input, stri)

            print("_______________________________________\n")

            print("\n",stri)
            print("_______________________________________")           
            continue
    return

    
def menu():
    
    #Checking for valid integer
    while True:
        inp = input("Choose the function you want to apply to your input: ")
        try:
            inp = int(inp)
            if 1 <= inp <= 6:
                return inp
            else:
                print("_______________________________________\n")
                print("Choose an integer between 1-6")
                print("_______________________________________\n")

        except ValueError:
            print("_______________________________________\n")
            print("Type a valid integer")
            print("_______________________________________\n")
            continue


def func(opt, stri):
    if opt == 1:
        stri = stri.lower()
        return stri
    elif opt == 2:
        stri = stri.upper()
        return stri
    elif opt == 3:
        stri = stri.capitalize()
        return stri
    elif opt == 4:
        stri = stri.title()
        return stri
    elif opt == 5:
        stri1 = stri.split()
        cleaned = " ".join(stri1)
        return cleaned

main()