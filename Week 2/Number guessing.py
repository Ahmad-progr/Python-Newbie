import random, time

def main():
    r_number = random.randint(1,100)
    guessed = False
    
    i = 5
    n = 1
    while i > 0:
        if guessed:
             break
        
        print(f"{i} guesses remaining!")
        time.sleep(1)
        guess = valid()

        if not guess:
             continue
        else:
            if i != 1:
                if guess > r_number:
                    print("Too high!")
                elif guess < r_number:
                    print("Too low!")
                else:
                    print(f"\nYou guessed correct number in {n} tries")
                    guessed = True

            elif i == 1:
                if guess > r_number or guess < r_number:
                    i -= 1
                    n += 1
                    break
                else:
                    print(f"\nYou guessed correct number in {n} tries")
                    guessed = True
            
        i -= 1
        n += 1
    
    if i == 0 and not guessed:
        time.sleep(1)
        print("-------------------------------------------------")
        print(f"The number to guess was {r_number}\nYou lost!")

def valid():
    try:
        n = int(input("Guess the number between 1-100: "))
        if n in range(1,101):
            return n
        else:
            print("Enter a guess between 1-100")
    except ValueError:
        print("------------------------")
        print("ENTER A VALID INTEGER")
        print("------------------------")
        return False


main()
