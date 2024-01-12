import re

str_to_int_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

rev_str_to_int_map = {key[::-1]: value for key, value in str_to_int_map.items()}

r_keys = "|".join([f"{str_num}" for str_num in str_to_int_map.keys()])
reverse_r_keys = "|".join(
    [f"{str_num[::-1]}" for str_num in str_to_int_map.keys()]
)


def get_cal(input_str):
    first_input_str = re.sub(
        r_keys, lambda match: str_to_int_map[match.group()], input_str, count=1
    )
    r = re.search(r"\d", first_input_str)
    first = r.group(0)
    second_input_str = re.sub(
        reverse_r_keys,
        lambda match: rev_str_to_int_map[match.group()],
        input_str[::-1],
        count=1,
    )[::-1]
    r = re.search(r"\d", second_input_str[::-1])
    second = r.group(0)
    return int(f"{first}{second}")


if __name__ == "__main__":
    with open("input.txt") as input_f:
        all_c = []
        for input_str in input_f.readlines():
            cal = get_cal(input_str)
            print(f"{input_str.strip()} {cal}")
            all_c.append(cal)
        sum = sum(all_c)
        print(sum)
