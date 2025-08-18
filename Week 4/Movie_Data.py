import sys

movies = [
    "Stranger Things",
    "The Hobbit: An Unexpected Journey",
    "The Hobbit: The Desolation of Smaug",
    "The Hobbit: The Battle of the Five Armies",
    "Pirates of the Caribbean: The Curse of the Black Pearl",
    "Pirates of the Caribbean: Dead Man’s Chest",
    "Pirates of the Caribbean: At World’s End",
    "Pirates of the Caribbean: On Stranger Tides",
    "Pirates of the Caribbean: Dead Men Tell No Tales",
    "Sound of Metal",
    "Shutter Island",
    "Extraction",
    "Extraction 2",
    "Titanic",
    "The Avengers",
    "Avengers: Age of Ultron",
    "Avengers: Infinity War",
    "Avengers: Endgame",
    "Iron Man",
    "Iron Man 2",
    "Iron Man 3",
    "Thor",
    "Thor: The Dark World",
    "Thor: Ragnarok",
    "Thor: Love and Thunder",
    "Justice League",
    "Inception",
    "Cruel Intentions",
    "The Curious Case of Benjamin Button",
    "Love & Other Drugs",
    "There Is No Evil",
    "Pride & Prejudice",
    "Game of Thrones",
    "Looking for Alaska",
    "Dark",
    "Truth or Dare",
    "Virgin Territory",
    "Fight Club",
    "12th Fail",
    "Dunki",
    "Fifty Shades of Grey",
    "365 Days",
    "Hacksaw Ridge",
    "Better Call Saul",
    "The Wild Robot",
    "Enola Holmes",
    "Enola Holmes 2",
    "John Wick",
    "John Wick: Chapter 2",
    "John Wick: Chapter 3 – Parabellum",
    "John Wick: Chapter 4",
    "The Pianist",
    "Front of the Class",
    "Drive",
    "Predestination",
    "The Green Mile",
    "We Live in Time",
    "Zodiac",
    "Dead Poets Society",
    "Me Before You",
    "The Lion King (2019)",
    "Little Women",
    "Good Will Hunting",
    "The Town",
    "The Girl Next Door",
    "The Gangster, The Cop, The Devil",
    "The Notebook",
    "Flyboys",
    "Before Sunrise",
    "Before Sunset",
    "Before Midnight",
    "The Secret Life of Walter Mitty",
    "Shershaah",
    "Maharaj",
    "The Words",
    "The Fault in Our Stars",
    "Lord of the Fireflies",
    "The Constant Gardener",
    "Anyone But You",
    "Zindagi Na Milegi Dobara",
    "Joyland",
    "Falling Down",
    "The Pursuit of Happyness",
    "Yeh Jawaani Hai Deewani",
    "Gloomy Sunday",
    "Se7en",
    "Cinderella Man",
    "Shithouse",
    "Udaan",
    "Materialists"
]

movies_strip = [m.lower() for m in movies]

def main():
    print("\n" + "-" * 50)
    print("        🌟 Welcome to Movie Tracker 🌟")
    print("-" * 50 + "\n")
    
    while True:
        name = input("🔍 Enter movie name: ").strip()
        print("-" * 50)
        check(name)
        print("-" * 50)
        if exit_program():
            print("\n")
            continue
        else:
            print("\n🍿 Thanks for using Movie Tracker! 🎬")
            sys.exit("Goodbye!")

def check(name):
    name = name.strip().lower()

    if name in movies_strip:
        print(f"✅ You have watched: {movies[movies_strip.index(name)]}")
    else:
        suggestions = [m for m in movies if name in m.lower()]
        if suggestions:
            print("🤔 Did you mean:")
            for i, s in enumerate(suggestions, start=1):
                print(f" {i}. {s}")
            try:
                opt = int(input("\nSelect option number: "))
                option = suggestions[opt - 1]
                print(f"✅ You have watched: {option}")
            except ValueError:
                print("⚠ Please enter a valid number.")
            except IndexError:
                print("⚠ Please select a valid option number.")
        else:
            print("❌ Not found!")
            if add_to_list():
                movies.append(name.title())
                movies_strip.append(name)
                print("✅ Movie added successfully!")
            else:
                print("ℹ Not added to the list.")

def exit_program():
    inp = input("\n🔄 Continue (Y/N)? ").strip().lower()
    if inp == "y":
        return True
    elif inp == "n":
        return False
    else:
        sys.exit("⚠ Cannot determine user choice, exiting...")

def add_to_list():
    inp = input("📌 Already watched (Y/N)? ").strip().lower()
    if inp == "y":
        return True
    elif inp == "n":
        return False
    else:
        sys.exit("⚠ Cannot determine user choice, exiting...")

main()
