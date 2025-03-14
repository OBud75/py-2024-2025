import collections


def find_middle_page(file_name: str):
    input = []

    with open(file_name) as input_file:
        line = input_file.readline()
        while line:
            input.append(line.strip())
            line = input_file.readline()

    divider = input.index("")
    edges, queries = input[:divider], input[divider + 1 :]
    graph = collections.defaultdict(set)

    for edge in edges:
        u, v = list(map(int, edge.split("|")))
        graph[u].add(v)

    ans = 0

    for query in queries:
        query = list(map(int, query.split(",")))
        good = True
        for i in range(len(query)):
            for j in range(i + 1, len(query)):
                if query[i] in graph[query[j]]:
                    good = False
        if good:
            ans += query[len(query) // 2]

    return ans

# Un peu les mêmes remarques que pour les autres jours:
# regardez enumerate, les iterateurs, générateurs et compréhensions de listes
print(find_middle_page("day5input.txt"))
