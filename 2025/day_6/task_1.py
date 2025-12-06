import math


def load_input():
    with open("input.txt", "r") as f:
        raw_lines = f.read().split("\n")

    lines = []
    for line in raw_lines:
        line = parse_line(line)
        lines.append(line)
    return lines


def parse_line(line):
    if "*" in line or "+" in line:
        return [x for x in line.split(" ") if x != ""]
    return [int(x) for x in line.split(" ") if x != ""]

def transpose(lines):
    return [list(x) for x in zip(*lines)]

def calculate_line(line):
    if "+" in line:
        return sum([int(x) for x in line if x != "+"])
    if "*" in line:
        return math.prod([int(x) for x in line if x != "*"])
    return None


def main():
    data = load_input()
    data = transpose(data)
    sum = 0
    for line in data:
        sum += calculate_line(line)

    print(data)
    print(sum)



if __name__ == "__main__":
    main()
