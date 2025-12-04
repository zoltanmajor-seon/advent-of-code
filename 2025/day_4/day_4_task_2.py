import copy


def load_input():
    with open("../day_5/day_4_input.txt", "r") as f:
        lines = f.read().split("\n")
    col_count = len(lines[0])
    printing_department = [["." for _ in range(col_count+2)]]

    for line in lines:
        print_line = ["."]
        print_line.extend(list(line))
        print_line.append(".")
        printing_department.append(print_line)
    printing_department.append(["." for _ in range(col_count+2)])

    return printing_department


def get_adjacent_elements(printing_department, row, col):
    if printing_department[row][col] == ".":
        return []
    adjacent_elements = []
    adjacent_elements.append(printing_department[row-1][col-1])
    adjacent_elements.append(printing_department[row-1][col])
    adjacent_elements.append(printing_department[row-1][col+1])
    adjacent_elements.append(printing_department[row][col-1])
    adjacent_elements.append(printing_department[row][col+1])
    adjacent_elements.append(printing_department[row+1][col-1])
    adjacent_elements.append(printing_department[row+1][col])
    adjacent_elements.append(printing_department[row+1][col+1])
    return adjacent_elements

def can_it_be_forklift(printing_department, row, col):
    print(f"Checking {row}, {col}")
    adjacent_elements = get_adjacent_elements(printing_department, row, col)
    if not adjacent_elements:
        print("Adjacent element count: out of bounds")
        return False
    else:
        print(f"Adjacent elemens: {adjacent_elements}")
        adjacent_elements_count = len([element for element in adjacent_elements if element == "@" or element == "x"])
        print(f"Adjacent element count: {adjacent_elements_count}")
    return adjacent_elements_count <= 3

def forklift_plan(printing_department, row_count, col_count):
    count_forklifted = 0
    for i in range(row_count):
        for j in range(col_count):
            if can_it_be_forklift(printing_department, i, j):
                count_forklifted += 1
                printing_department[i][j] = "x"
    return count_forklifted, printing_department


def remove_characters(param, printing_department, row_count, col_count):
    for i in range(row_count):
        for j in range(col_count):
            if printing_department[i][j] == param:
                printing_department[i][j] = "."
    return printing_department


def main():
    printing_department = load_input()
    row_count = len(printing_department)
    col_count = len(printing_department[0])
    total_forklifted_count = 0
    for i in range(row_count * col_count):
        count_forklifted, printing_department = forklift_plan(printing_department, row_count, col_count)
        total_forklifted_count += count_forklifted
        if count_forklifted == 0:
            break
        printing_department = remove_characters('x', printing_department, row_count, col_count)

    print()
    for i in range(row_count):
        print(" ".join(printing_department[i]))
    print()

    print(total_forklifted_count)

if __name__ == "__main__":
    main()

