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
        # On peut faire une compréhension de liste avec condition, cela ressemblerait à quelque chose comme
        # sum(1 for report in [list(map(int, line.split())) for line in file] if is_safe(report))
        # Ou en regardant le nombre de reports dans la liste des reports qui sont safe.
        # len([report for report in [list(map(int, line.split())) for line in file] if is_safe(report)])

    return safe_count

print(count_safe_reports())
