students = []

with open("Week 6/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


for su in sorted(students, key=get_name):
    print(f"{su['name']} is in {su['house']} house")