
def findGuard(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in '^>v<':
                return (x, y, cell)
    return None


def turnRight(direction):
    directions = '^>v<'
    return directions[(directions.index(direction) + 1) % 4]


def moveForward(x, y, direction):
    if direction == '^':
        return (x, y - 1)
    elif direction == '>':
        return (x + 1, y)
    elif direction == 'v':
        return (x, y + 1)
    elif direction == '<':
        return (x - 1, y)


def simulateGuard(grid):
    x, y, direction = findGuard(grid)
    visited_positions = set()
    visited_positions.add((x, y))

    while True:
        new_x, new_y = moveForward(x, y, direction)
        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]) or grid[new_y][new_x] == '#':
            direction = turnRight(direction)
        else:
            x, y = new_x, new_y
            visited_positions.add((x, y))

        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
            break

    return len(visited_positions)


def readFileAsGrid(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid

grid = readFileAsGrid('data.txt')
result = simulateGuard(grid)
print("Number of distinct positions visited:", result)