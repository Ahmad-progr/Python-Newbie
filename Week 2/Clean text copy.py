def main():
    stri = input("Type: ").strip()

    print("\n1. All lowercase",
        "\n2. First letter of input capitalized", 
        "\n3. All uppercase",
        "\n4. First letter of each word capitalize",
        "\n5. Remove extra whitespaces in input"
        "\n6.  Quit program")
    
    print("_______________________________________\n")
    
    get_input = menu()
    if get_input == 6:
        return
    else:
        opt_select = func(get_input, stri)

        print("_______________________________________\n")

        print(opt_select,"\n")

#    formatted_str = cleaning(stri)
#   print(formatted_str)

def menu():
    
    #Checking for valid integer
    while True:
        inp = input("Choose the function you want to apply to your input: ")
        try:
            inp = int(inp)
            if inp < 1 or inp > 6:
                print("Choose an integer between 1-6\n")
                continue

        except ValueError:
            print("Type a valid integer\n")
            continue
        break

    #Choosing menu option
    match inp:
        case 1: return inp
        case 2: return inp
        case 3: return inp
        case 4: return inp
        case 5: return inp
        case 6: return inp

def func(opt, stri: str):
    if opt == 1:
        stri = stri.lower()
        return stri
    elif opt == 2:
        stri = stri.capitalize()
        return stri
    elif opt == 3:
        stri = stri.upper()
        return stri
    elif opt == 4:
        stri = stri.title()
        return stri
    elif opt == 5:
        stri1 = stri.split()
        cleaned = " ".join(stri1)
        return cleaned
   # words = text.lower().capitalize().strip().split()
   # cleaned = " ".join(words)
   # return cleaned

main()