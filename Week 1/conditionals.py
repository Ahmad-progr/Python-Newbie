x = int(input("What's x? "))
y = int(input("What's y? "))

if x>y:
    print(f'"{x} is greater than {y}"')
elif y>x:
    print(f'"{y} is greater than {x}"')
else:
    print(f'"Both {x} and {y} are equal"')