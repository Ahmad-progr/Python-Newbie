import inflect

p = inflect.engine()
names = []


def main():
    while True:
        try:
            n = input("Name: ")
            names.append(n)
        except EOFError:
            print()
            break

    name = p.join(names)
    print("Adeiu, adeiu to", name)


main()
