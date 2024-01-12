import re

numbers = []
stars = {}

with open("input.txt") as f:
    for row, line in enumerate(f.readlines()):
        for match in re.finditer(r"\d+", line):
            numbers.append(
                {
                    "value": int(match.group()),
                    "row": row,
                    "span": (match.span()[0], match.span()[1] - 1),
                }
            )
        for match in re.finditer(r"[\*]+", line):
            stars[(row, match.span()[0])] = []

star_row_to_cols = {}
for key in stars:
    if key[0] in stars:
        star_row_to_cols[key[0]].add(key[1])
    else:
        star_row_to_cols[key[0]] = {key[1]}

for number in numbers:
    for i, star in enumerate(stars):
        if (
            number["row"] - 1 <= star[0] <= number["row"] + 1
            and number["span"][0] - 1 <= star[1] <= number["span"][1] + 1
        ):
            stars[star].append(number["value"])
gear_ratios = []
for star in stars:
    if len(stars[star]) == 2:
        gear_ratios.append(stars[star][0] * stars[star][1])
print(sum(gear_ratios))
