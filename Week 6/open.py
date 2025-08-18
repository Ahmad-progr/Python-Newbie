import sys

print("1. Add to file\n2. Read from file\n3. Remove all data")
opt = int(input(">> "))

if opt == 1:
    print("How many names? ")
    n = int(input(">> "))
    for _ in range(n):
        name = input("Add name: ").strip().capitalize()
        with open("Week 6/names.txt", "a") as file:
            file.write(f"{name}\n")

elif opt == 2:
    with open("Week 6/names.txt") as file:
        contents = file.read()
        if not contents.strip():
            sys.exit(">> No names saved\n")
        else:
            print("         --NAMES SAVED IN FILE--")
            for name in sorted(contents.splitlines()):
                print(name)

elif opt == 3:
    with open("Week 6/names.txt", "r+") as file:
        contents = file.read()
        if not contents.strip():
            sys.exit(">> File already empty\n")
        else:
            file.seek(0)
            file.truncate()
            sys.exit(">> Successfully removed all contents\n")

else:
    sys.exit("Choose valid option")
