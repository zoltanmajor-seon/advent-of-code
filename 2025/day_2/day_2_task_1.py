def load_input():
    with open("day_2_input.txt", "r") as f:
        return f.read().split(",")

def generate_ids(id_range):
    range_low = id_range.split("-")[0]
    range_high = id_range.split("-")[1]
    return range(int(range_low), int(range_high) + 1)


def is_valid(id):
    if len(str(id)) % 2 != 0:
        return True

    first_half = str(id)[:len(str(id)) // 2]
    second_half = str(id)[len(str(id)) // 2:]

    if first_half == second_half:
        return False

    return True

def main():
    id_ranges = load_input()
    ids = set()
    valid_ids = set()
    invalid_ids = set()
    sum_invalid_ids = 0
    sum_valid_ids = 0
    for id_range in id_ranges:
        for id in generate_ids(id_range):
            ids.add(id)
    for id in ids:
        if is_valid(id):
            sum_valid_ids += id
            valid_ids.add(id)
        else:
            sum_invalid_ids += id
            invalid_ids.add(id)
    print(invalid_ids)
    print(sum_invalid_ids)




if __name__ == "__main__":
    main()
