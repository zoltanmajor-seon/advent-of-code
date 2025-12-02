def load_input():
    with open("day_2_input.txt", "r") as f:
        return f.read().split(",")

def generate_ids(id_range):
    range_low = id_range.split("-")[0]
    range_high = id_range.split("-")[1]
    return range(int(range_low), int(range_high) + 1)

def is_valid(id):
    is_valid = True
    for i in range(len(str(id))-1):
        is_valid = is_valid_advanced_by_seq(id, i+1)
        if not is_valid:
            break
    return is_valid


def is_valid_advanced_by_seq(id, split_size):
    if len(str(id)) % split_size != 0:
        return True

    splits = {str(id)[i:i + split_size] for i in range(0, len(str(id)), split_size)}

    if len(splits) == 1:
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
