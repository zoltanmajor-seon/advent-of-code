
def load_input():
    with open("day_5_input.txt", "r") as f:
        lines = f.read().split("\n\n")

    fresh_ids_ranges = lines[0].split("\n")
    fresh_ids_ranges = [[int(x.split("-")[0]), int(x.split("-")[1]) + 1] for x in fresh_ids_ranges]
    available_ingredient_ids = lines[1].split("\n")

    return fresh_ids_ranges, available_ingredient_ids


def merge_intervals(intervals):
    # Sort intervals based on start values
    intervals.sort()

    res = []
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]

        # If current interval overlaps with the last merged
        # interval, merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

def ingredient_id_is_fresh(fresh_ids_ranges, available_ingredient_id):
    for fresh_id_range in fresh_ids_ranges:
        if available_ingredient_id >= fresh_id_range[0] and available_ingredient_id < fresh_id_range[1]:
            return available_ingredient_id
    return None

def find_available_ingredient_ids(fresh_ids_ranges, available_ingredient_ids):
    fresh_ids = []
    count = 0
    for available_ingredient_id in available_ingredient_ids:
        if ingredient_id_is_fresh(fresh_ids_ranges, available_ingredient_id):
            fresh_ids.append(available_ingredient_id)
            count += 1
    return fresh_ids, count

def main():
    fresh_ids_ranges, available_ingredient_ids = load_input()


    available_ingredient_ids = [int(item) for item in available_ingredient_ids]
    available_ingredient_ids.sort()


    print(fresh_ids_ranges)
    print(len(fresh_ids_ranges))
    print(available_ingredient_ids)

    fresh_ids_ranges = merge_intervals(fresh_ids_ranges)

    print(fresh_ids_ranges)
    print(len(fresh_ids_ranges))


    fresh_ids, count = find_available_ingredient_ids(fresh_ids_ranges, available_ingredient_ids)
    print(fresh_ids)
    print(count)

if __name__ == "__main__":
    main()
