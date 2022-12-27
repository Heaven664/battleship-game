import cowsay

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
fleet = ("F3", "F2", "F1", "B9", "C9", "D9", "E9", "A6", "A7", "A5", "I9", "J9", "D3", "D4", "F6", "G6", "J2", "I7", "A1","D7")
bombs = ["G10", "G8", "J5", "H3", "J3", "A3"]
spotted = []
lives = 3
MAX_LIVES = 3
killed = 0
rules = """
    🐳Welcome onboard, Captain\n

    🐳If you've played this game before - type 'y' to start the game\n
    🐳Rules are very simple, you just have to sink the enemy fleet
    🐳But be careful, Captain Henry Every left some mines on battlefield, don't jump on them
    🐳You can target only one cell at a time, when your crew is ready, they will ask you for coordinates
    🐳A coordinate is a 'column name' + 'row number'. Like 'B7', 'j10', 'A1'\n
    🐳If you are ready type 'y' to start the fight
    🐀Or type 'n' if you are afraid\n
    Your order: """

def farewell():
    cowsay.tux("🐳 See you next time 🐳")