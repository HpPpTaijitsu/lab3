def longest_path(matrix, start_char):
    """
    Поиск длины самого длинного пути в матрице,
    начинающегося с заданного
    символа. Символы в пути должны следовать
    в алфавитном порядке без пропусков.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    memo = [[-1] * cols for _ in range(rows)]

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def dfs(x, y):
        if memo[x][y] != -1:
            return memo[x][y]

        max_len = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if ord(matrix[nx][ny]) == ord(matrix[x][y]) + 1:
                    max_len = max(max_len, 1 + dfs(nx, ny))

        memo[x][y] = max_len
        return max_len

    max_path = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                max_path = max(max_path, dfs(i, j))

    return max_path


if __name__ == "__main__":
    my_matrix = [
        ["C", "D", "E", "F", "G"],
        ["B", "C", "D", "E", "F"],
        ["A", "B", "C", "D", "E"],
        ["B", "C", "D", "E", "F"],
        ["C", "D", "E", "F", "G"],
    ]

    start_char = "C"

    print("Матрица (5x5):")
    for row in my_matrix:
        print(" ".join(row))

    result = longest_path(my_matrix, start_char)
    print(
        f"\nДлина самого длинного пути, начинающегося с '{start_char}': "
        f"{result}"
    )
