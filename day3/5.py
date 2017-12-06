from enum import Enum
class Direction(Enum):
    RIGHT = 1
    UP    = 2
    LEFT  = 3
    DOWN  = 4

cols_count = 600
rows_count = 600
destination = 347991

matrix = [[0 for x in range(cols_count)] for x in range(rows_count)]

x = int(cols_count / 2) - 1
y = int(cols_count / 2) - 1
d = Direction.DOWN
for i in range(destination + 1):
    while matrix[x][y] != 0:
        # print(f"matrix[{x}][{y}] == {matrix[x][y]}")
        if d == Direction.RIGHT:
            x = x + 1
        elif d == Direction.UP:
            y = y + 1
        elif d == Direction.LEFT:
            x = x - 1
        elif d == Direction.DOWN:
            y = y - 1
    matrix[x][y] = i
    if d == Direction.RIGHT and matrix[x][y+1] == 0:
        d = Direction.UP
    elif d == Direction.UP and matrix[x-1][y] == 0:
        d = Direction.LEFT
    elif d == Direction.LEFT and matrix[x][y-1] == 0:
        d = Direction.DOWN
    elif d == Direction.DOWN and matrix[x+1][y] == 0:
        d = Direction.RIGHT

steps = 0
while matrix[x][y] != 1:
    print(f"matrix[{x}][{y}] == {matrix[x][y]}")
    min = float("inf")
    xdiff = 0
    ydiff = 0
    if matrix[x+1][y] != 0 and matrix[x+1][y] < min:
        min = matrix[x+1][y]
        xdiff = 1
        ydiff = 0
    if matrix[x-1][y] != 0 and matrix[x-1][y] < min:
        min = matrix[x-1][y]
        xdiff = -1
        ydiff = 0
    if matrix[x][y+1] != 0 and matrix[x][y+1] < min:
        min = matrix[x][y+1]
        xdiff = 0
        ydiff = 1
    if matrix[x][y-1] != 0 and matrix[x][y-1] < min:
        min = matrix[x][y-1]
        xdiff = 0
        ydiff = -1
    x = x + xdiff
    y = y + ydiff
    steps = steps + 1

# print('\n'.join([''.join(['{:4}'.format(item) for item in row])
#       for row in matrix]))
print(steps)
