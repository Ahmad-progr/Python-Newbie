def main():
    v_hour = get_hour()
    greeting = hour_check(v_hour)
    print(greeting)

def get_hour():
    while True:
        t = input("Enter time in 24 hour format (e.g. 14:30): ")

        if ':' not in t or t.count(':') != 1:
            print("Invalid Format")
            continue

        parts = t.split(":")

        if not parts[0].isdigit() or not parts[1].isdigit():
            print("Enter a numeric value")
            continue

        h = int(parts[0])
        m = int(parts[1])

        if not (0 <= h <= 23 and 0 <= m <= 59):
            print("Invalid Time")
            continue

        return h

def hour_check(hour):
    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

main()
