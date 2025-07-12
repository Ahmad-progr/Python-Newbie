def main():
    print("What do you want to repeat?")
    while True:
        user_input = input("Input| ")

        if len(user_input) == 0:
            print("Type anything to repeat or type /exit to quit")
            continue
        elif user_input == '/exit':
            print('Bye!')
            return
        break
    
    print("_______________________________________\n")

    while True:
        
        inp_iteration = input("How many times| ")



        try:
            inp_iteration = int(inp_iteration)
        except ValueError:
            print("\nPlease enter valid integer\n")
            continue
        break

    print("_______________________________________")
    
    if inp_iteration <= 0:
        print(f'\n"Since you entered a negative iteration"')
        i = 0
        print(f"\nRepeat {user_input} {-inp_iteration} times:")
        while i > inp_iteration:
            u_input = input('\n')
            if u_input == user_input:
                i -= 1

            else:
                print("Repeat what you typed: ")
                continue
        
        print("_______________________________________\n")
        print("Great Job!".center(40,' '))   
    
    else:
        print("_______________________________________\n")
        f_loop(user_input, inp_iteration)
        print("\n")

    
def f_loop(user_input, inp_iteration):
    for _ in range(inp_iteration):
        print(user_input)


main()