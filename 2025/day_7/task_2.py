def load_input():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n\n")

    return lines


def main():
    data = load_input()
    print(data)


if __name__ == "__main__":
    main()