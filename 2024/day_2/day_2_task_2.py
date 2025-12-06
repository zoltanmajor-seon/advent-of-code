import copy


def load_input():
    with open("input.txt", "r") as f:
        raw_reports = f.read().split("\n")
    reports = []
    for raw_report in raw_reports:
        reports.append([int(level) for level in raw_report.split(" ")])
    return reports

def get_slope(first, second):
    if first == second:
        return "constant"
    if first < second:
        return "increasing"
    return "decreasing"

def get_distance(first, second):
    return abs(first - second)

def check_report(report):
    slope = get_slope(report[0], report[1])
    if slope == "constant":
        return False, 0

    if slope == "increasing":
        for i in range(len(report)-1):
            if get_slope(report[i], report[i+1]) != "increasing":
                return False, i
            if get_distance(report[i], report[i+1]) > 3:
                return False, i

    if slope == "decreasing":
        for i in range(len(report)-1):
            if get_slope(report[i], report[i+1]) != "decreasing":
                return False, i
            if get_distance(report[i], report[i+1]) > 3:
                return False, i

    return True, None


def main():
    reports = load_input()
    safe_report_count = 0
    for report in reports:

        is_safe, middle_index = check_report(report)

        if is_safe:
            safe_report_count += 1
        else:
            report_1 = copy.deepcopy(report)
            report_2 = copy.deepcopy(report)
            del report_1[middle_index-1]
            del report_2[middle_index+1]
            del report[middle_index]

            is_safe_1, _ = check_report(report_1)
            is_safe_2, _ = check_report(report_2)
            is_safe_3, _ = check_report(report)

            if any([is_safe_1, is_safe_2, is_safe_3]):
                safe_report_count += 1

    print(safe_report_count)


if __name__ == "__main__":
    main()
