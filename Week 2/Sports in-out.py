games = {
    "Badminton": "Indoor",
    "Chess": "Indoor",
    "Ludo": "Indoor",
    "Football": "Outdoor",
    "Basketball": "Outdoor",
    "Tug o War": "Outdoor",
    "Volley Ball": "Outdoor",
    "Poker": "Indoor",
    "Cricket": "Outdoor"
}

def main():
    game = input("\nEnter a game: ").title()
    if game in games:
        print(game_ground(game))
    else:
        print("===================================\nGame not found.\n===================================")

def game_ground(game):
    return f"\n===================================\n\n{game} is an {games[game]} game.\n\n==================================="

main()
