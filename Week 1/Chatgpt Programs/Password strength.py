def main():
        password = p_length()
        if password:
            if p_valid(password):
                print("Strong Password!")

def p_length():
    while True:
        p = input('Choose a password: ')
        pass_len = len(p)

        if pass_len < 4:
            print("Your password should be at least 4 characters")
            continue
        else:
            return p
        
def p_valid(pw):
    has_digit = False
    has_al = False
    for char in pw:
        if char.isdigit():
            has_digit = True
        if char.isalpha():
            has_al = True

    if has_digit and has_al:
        return True
    else:
        print("Your password should contain atleast one alphabet and one number")
        return False
main()