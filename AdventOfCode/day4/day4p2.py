def find_all_occurrences(graph):
    rows, cols = len(graph), len(graph[0])
    valid = ["MAS", "SAM"]
    ans = 0

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == "A" and 0 < i < rows - 1 and 0 < j < cols - 1:
                pos_diagonal = "".join(
                    [graph[i + 1][j - 1], graph[i][j], graph[i - 1][j + 1]]
                )
                neg_diagonal = "".join(
                    [graph[i - 1][j - 1], graph[i][j], graph[i + 1][j + 1]]
                )
                if pos_diagonal in valid and neg_diagonal in valid:
                    ans += 1

    return ans


graph = []
with open("day4input.txt") as input_file:
    line = input_file.readline()
    while line:
        graph.append(line.strip())
        line = input_file.readline()


occurrences = find_all_occurrences(graph)
print(occurrences)
