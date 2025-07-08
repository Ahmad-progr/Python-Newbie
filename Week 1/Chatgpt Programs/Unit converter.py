def main():
    print("e.g. 10 inches to cm")
    u_inp = input("Convert: ").strip().lower()

    parts = u_inp.split()

    if len(parts) != 4 or parts[2] != "to":
        print("Invalid Format 🤕")
        return

    value = parts[0]
    f_unit = parts[1]
    t_unit = parts[3]

    try:
        num = float(value)
    except ValueError:
        print("Enter a valid number 🤕")
        return
    
    result = convert(num, f_unit, t_unit)

    if result is None:
        print("Conversion not supported 🤕")
    else:
        print(f"{num} {f_unit} is {round(result, 2)} {t_unit}")


def convert(value, f_unit, t_unit):
    if f_unit in ["inches", "inch"] and t_unit == "cm":
        return value * 2.54
    elif f_unit == "cm" and t_unit in ["inches", "inch"]:
        return value / 2.54
    elif f_unit in ["kg", "kilograms", "kgs"] and t_unit in ["pounds", "pound"]:
        return value * 2.2
    elif f_unit in ["pound", "pounds"] and t_unit in ["kgs", "kilograms", "kg"]:
        return value / 2.2
    else:
        return None
    

main()