def load_input():
    with open("task_1_input.txt", "r") as f:
        return f.read().split("\n")


def calculate_zeros_crossed(current_point):
    zero_crossed = 0
    if current_point < 0:
        current_point = current_point % 100
    elif current_point > 99:
        current_point = current_point % 100
    if current_point == 0:
        zero_crossed += 1
    return zero_crossed


def main():

    current_point = 50
    zero_crossed = 0
    rotations = load_input()
    previous_point = 50
    for rotation in rotations:
        if rotation.startswith("R"):
            current_point += int(rotation[1:])
        elif rotation.startswith("L"):
            current_point -=int(rotation[1:])
        zero_crossed_in_rotation, current_point = calculate_zeros_crossed(int(current_point))
        zero_crossed += zero_crossed_in_rotation
        previous_point = current_point
        print(rotation, zero_crossed_in_rotation, current_point)

    print(zero_crossed)



if __name__ == "__main__":
    main()
