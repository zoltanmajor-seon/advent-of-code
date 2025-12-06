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

def is_safe(report):
    slope = get_slope(report[0], report[1])
    if slope == "constant":
        return False

    if slope == "increasing":
        for i in range(len(report)-1):
            if get_slope(report[i], report[i+1]) != "increasing":
                return False
            if get_distance(report[i], report[i+1]) > 3:
                return False

    if slope == "decreasing":
        for i in range(len(report)-1):
            if get_slope(report[i], report[i+1]) != "decreasing":
                return False
            if get_distance(report[i], report[i+1]) > 3:
                return False

    return True


def main():
    reports = load_input()
    safe_report_count = 0
    for report in reports:
        if is_safe(report):
            safe_report_count += 1
    print(reports)
    print(safe_report_count)


if __name__ == "__main__":
    main()
