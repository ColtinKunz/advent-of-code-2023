powers = []

with open("input.txt") as f:
    for line in f.readlines():
        game_and_id, draws = tuple(line.strip().split(": "))
        game_id = int(game_and_id.replace("Game ", ""))
        over_max = False
        max_game = {"red": 0, "green": 0, "blue": 0}
        for draw in draws.split("; "):
            for hand in draw.split(", "):
                number, color = tuple(hand.split(" "))
                if max_game[color] < int(number):
                    max_game[color] = int(number)
        powers.append(max_game["red"] * max_game["blue"] * max_game["green"])

print(sum(powers))
