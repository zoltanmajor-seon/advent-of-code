import math


def load_input():
    with open("input.txt", "r") as f:
        raw_lines = f.read().split("\n")

    raw_lines = right_pad_lines_with_spaces_to_equal_length(raw_lines)

    return raw_lines, len(raw_lines)

def right_pad_lines_with_spaces_to_equal_length(raw_lines):
    maximum_line_length = max([len(line) for line in raw_lines])
    print(maximum_line_length)
    for index, line in enumerate(raw_lines):
        if len(line) < maximum_line_length:
            raw_lines[index] = line + " " * (maximum_line_length - len(line))

        print(index, len(raw_lines[index]))

    return raw_lines

def get_number_by_index(data, index):
    number = ""
    for line in data:
        number += line[index]
    return int(number.strip()) if number.strip() != "" else None


def get_next_homework_task(operators, i):
    for j in range(i, len(operators)):
        if operators[j] != " " or j == len(operators):
            return j
    return len(operators)


def fetch_homework_task(data, index_start, index_stop):
    operators = data[-1]
    raw_numbers = data[:-1]
    numbers = [get_number_by_index(raw_numbers, i) for i in range(index_start, index_stop) if get_number_by_index(raw_numbers, i) is not None]
    return operators[index_start], numbers


def get_homework_task(data):
    operators = data[-1]
    for i in range(len(operators)):
        if operators[i] != " ":
            index_stop = get_next_homework_task(operators, i + 1)
            yield fetch_homework_task(data, i, index_stop)


def calculate_homework(homework):
    operator, numbers = homework
    if operator == "+":
        return sum(numbers)
    if operator == "*":
        return math.prod(numbers)


def main():
    data, length = load_input()
    print(data)
    sum = 0
    for homework in get_homework_task(data):
        sum += calculate_homework(homework)

    print(sum)







if __name__ == "__main__":
    main()
