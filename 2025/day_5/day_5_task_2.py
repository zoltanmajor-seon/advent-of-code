
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


def add_intervals(fresh_ids_ranges):
    return sum([x[1] - x[0] for x in fresh_ids_ranges])


def main():
    fresh_ids_ranges, _ = load_input()
    fresh_ids_ranges = merge_intervals(fresh_ids_ranges)
    print(fresh_ids_ranges)

    count_fresh_ids = add_intervals(fresh_ids_ranges)
    print(count_fresh_ids)

if __name__ == "__main__":
    main()
