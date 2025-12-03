def load_input():
    with open("day_3_input.txt", "r") as f:
        return f.read().split("\n")

def get_highest_digit(bank):
    bank_digits =[int(digit) for digit in  list(bank)]
    maximum = max(bank_digits)
    maximum_index = bank_digits.index(maximum)
    return maximum, maximum_index


def get_joltage(bank, length):
    digit_indexes = []
    digits = []
    start_from = 0
    for digit in range(length-1, -1, -1):
        end = -digit if digit !=0 else None
        highest_digit, highest_digit_index = get_highest_digit(bank[start_from:end])
        digit_indexes.append(highest_digit_index)
        digits.append(str(highest_digit))
        start_from += highest_digit_index + 1

    joltage = int("".join(digits))

    print(f"{bank} -> {joltage} -> {digit_indexes} -> {digits}")
    return joltage

def main():
    banks = load_input()
    print(banks)
    joltage = 0
    for bank in banks:
        joltage += get_joltage(bank,12)
    print(joltage)

if __name__ == "__main__":
    main()
