def main():
    time = input("What time is it? ").strip()
    am_time = time.lower().endswith("a.m.")
    pm_time = time.lower().endswith("p.m.")
    float_time = convert(time)
    if float_time != None:
        if am_time:
            if 7 <= float_time <= 8:
                print("breakfast time")
        elif pm_time:
            if 12 <= float_time <= 13:
                print("lunch time")
            elif 6 <= float_time <= 7:
                print("dinner time")
        elif not am_time and not pm_time:
            if " " in time:
                return
            else:
                if 18 <= float_time <= 19:
                    print("dinner time")
                elif 7 <= float_time <= 8:
                    print("breakfast time")
                elif 12 <= float_time <= 13:
                    print("lunch time")
    else:
        return


def convert(time):
    if " " in time:
        time1, zone = time.split(" ")
        hours, minutes = time1.split(":")
    else:
        hours, minutes = time.split(":")

    minutes  = int(minutes)
    hours = int(hours)

    if 0 <= minutes <= 59 and 0 <= hours <= 23:
        minutes = (minutes * 100) / 60
        conv_min = float(minutes / 100)
        new_time = hours+conv_min
        return new_time
    else:
        return None

if __name__ == "__main__":
    main()
