import random
from collections import defaultdict

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

given = defaultdict(list)

for turn in range(4):
    print(f"---- Turn {turn + 1} ----")
    i = 0
    while i < 10:
        suit = random.choice(suits)
        rank = random.choice(ranks)

        if rank not in given[suit]:
            given[suit].append(rank)
            print(f"{rank} of {suit}")
            i += 1

    print()
