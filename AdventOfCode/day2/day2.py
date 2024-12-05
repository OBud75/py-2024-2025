def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    all_increasing = all(0 < diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff < 0 for diff in differences)

    return all_increasing or all_decreasing


def count_safe_reports():
    safe_count = 0

    with open("./day2input.txt", "r") as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1

    return safe_count

print(count_safe_reports())
