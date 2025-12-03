def load_input():
    with open("day_3_input_test.txt", "r") as f:
        return f.read().split("\n")

def get_highest_digit(bank):
    bank_digits =[int(digit) for digit in  list(bank)]
    maximum = max(bank_digits)
    maximum_index = bank_digits.index(maximum)
    return maximum, maximum_index


def get_joltage(bank):
    first_digit, first_digit_index = get_highest_digit(bank[:-1])
    second_digit, second_digit_index = get_highest_digit(bank[first_digit_index+1:])
    second_digit_index += first_digit_index + 1
    joltage = int(f"{first_digit}{second_digit}")
    # print the bank string with the first_digit_index and second_digit_index highlighted
    bank = bank[:first_digit_index] + "(" + bank[first_digit_index] + ")" + bank[first_digit_index+1:second_digit_index] + "(" + bank[second_digit_index] + ")" + bank[second_digit_index+1:]
    print(f"{bank} -> {joltage}")
    return joltage

def main():
    banks = load_input()
    print(banks)
    joltage = 0
    for bank in banks:
        joltage += get_joltage(bank)
    print(joltage)

if __name__ == "__main__":
    main()
