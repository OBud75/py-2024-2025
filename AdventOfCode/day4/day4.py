def find_all_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def count_from_position(x, y):
        count = 0
        for dx, dy in directions:
            if all(
                is_valid(x + dx * k, y + dy * k)
                and grid[x + dx * k][y + dy * k] == word[k]
                for k in range(word_len)
            ):
                count += 1
        return count

    total_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                total_count += count_from_position(i, j)

    return total_count


with open("./day4input.txt", "r") as file:
    input_data = file.read().strip().splitlines()

grid = [list(line) for line in input_data]

word = "XMAS"

occurrences = find_all_occurrences(grid, word)
print(occurrences)
