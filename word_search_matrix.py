def find_words(board, dictionary):
    """
    Находит все слова из словаря, которые можно составить из матрицы,
    двигаясь в любом из 8 направлений.

    Args:
        board: 2D список символов (матрица M x N)
        dictionary: список слов для поиска

    Returns:
        Множество найденных слов
    """
    rows = len(board)
    cols = len(board[0])

    found_words = set()

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    def dfs(x, y, word, index, visited):
        if index == len(word):
            return True

        if not (0 <= x < rows and 0 <= y < cols):
            return False
        if visited[x][y] or board[x][y] != word[index]:
            return False

        visited[x][y] = True

        for dx, dy in directions:
            if dfs(x + dx, y + dy, word, index + 1, visited):
                visited[x][y] = False
                return True

        visited[x][y] = False
        return False

    for word in dictionary:
        visited = [[False] * cols for _ in range(rows)]
        found = False
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word, 0, visited):
                    found_words.add(word)
                    found = True
                    break
            if found:
                break

    return found_words


if __name__ == "__main__":
    my_board = [
        ['К', 'О', 'Т'],
        ['Р', 'А', 'Н'],
        ['С', 'Л', 'О'],
    ]

    my_dictionary = ['КОТ', 'РАН', 'СОН', 'ЛОСЬ', 'НОС', 'ТОР', 'РОТ', 'КОРА']

    print("\nМатрица 3x3:")
    for row in my_board:
        print(' '.join(row))

    print(f"\nСловарь: {my_dictionary}")

    found = find_words(my_board, my_dictionary)

    print(f"\nНайденные слова: {found}")