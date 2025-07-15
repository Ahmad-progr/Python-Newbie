def main():
    sentence = input("Input: ")
    counts = vowel_count(sentence)

    print("Output:",)
    for vowel, count in counts.items():
        if count > 0:
            print(f"Vowel {vowel} is {count} times.  ")

def vowel_count(sentence):
    counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for char in sentence.lower():
        if char in counts:
            counts[char] += 1
    return counts

main()
