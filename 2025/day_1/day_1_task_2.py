def load_input():
    with open("task_1_input.txt", "r") as f:
        return f.read().split("\n")


def calculate_zero_crossed_upgraded(current_point: int, previous_point: int):
    was_previous_zero = previous_point == 0
    if current_point == 0:
        return 1, 0
    zero_crossed = 0
    if current_point < 0 and not was_previous_zero:
        zero_crossed += int((abs(current_point) + 100) / 100)
        current_point = current_point % 100
    elif current_point > 99:
        zero_crossed += abs(int(current_point / 100))
        current_point = current_point % 100
    elif current_point < 0 and was_previous_zero:
        zero_crossed += int((abs(current_point)) / 100)
        current_point = current_point % 100
    return zero_crossed, current_point

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
        zero_crossed_in_rotation, current_point = calculate_zero_crossed_upgraded(int(current_point), previous_point)
        zero_crossed += zero_crossed_in_rotation
        previous_point = current_point
        print(rotation, zero_crossed_in_rotation, current_point)

    print(zero_crossed)



if __name__ == "__main__":
    main()
