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


def countXmax():
    total = 0
    with open('data.txt') as f:
        lines = f.readlines()

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if x + 2 < len(lines[y]) and y + 2 < len(lines):
                if (lines[y][x] == 'M' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x + 2] == 'S') or (lines[y][x] == 'S' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x + 2] == 'M'):
                    if (lines[y][x + 2] == 'M' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x] == 'S') or (lines[y][x + 2] == 'S' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x] == 'M'):
                        total += 1
    return total

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
      countXmax()} times in the grid.")
