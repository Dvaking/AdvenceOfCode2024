def searchWordInGrid(grid, word):
    def searchFromPosition(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (1, 0),
        (0, 1),
        (1, 1),
        (1, -1),
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-1, 1)
    ]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if searchFromPosition(i, j, dx, dy):
                    count += 1
    return count


def countXmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def isXmas(x, y):
        try:
            diag1 = (
                (grid[x - 1][y - 1] == 'M' and grid[x][y] == 'A' and grid[x + 1][y + 1] == 'S') or
                (grid[x - 1][y - 1] == 'S' and grid[x][y]
                 == 'A' and grid[x + 1][y + 1] == 'M')
            )
            diag2 = (
                (grid[x - 1][y + 1] == 'M' and grid[x][y] == 'A' and grid[x + 1][y - 1] == 'S') or
                (grid[x - 1][y + 1] == 'S' and grid[x][y]
                 == 'A' and grid[x + 1][y - 1] == 'M')
            )
            return diag1 or diag2
        except IndexError:
            return False

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if isXmas(i, j):
                count += 1

    return count

def readFileAsGrid(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid


exemple = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX'
]
exemple2 = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    ".........."
]

filename = 'data.txt'
output = readFileAsGrid(filename)
word = 'XMAS'
print(f"The word '{word}' appears {
      searchWordInGrid(output, word)} times in the grid.")
print(f"The word '{word}' appears {
      countXmas(output)} times in the grid.")
