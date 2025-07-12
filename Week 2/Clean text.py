def main():
    stri = input("Type: ")

    formatted_str = cleaning(stri)
    print(formatted_str)

def cleaning(text: str):
    words = text.lower().capitalize().strip().split()
    cleaned = " ".join(words)
    return cleaned

main()