words = {}
def main():
    sentence = input("Input: ").lower()

    for word in sentence.split():
        if word not in words:
            words[word] = True

    print(words.keys())
main()