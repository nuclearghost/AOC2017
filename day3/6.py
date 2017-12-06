from enum import Enum
class Direction(Enum):
    RIGHT = 1
    UP    = 2
    LEFT  = 3
    DOWN  = 4

cols_count = 1000
rows_count = 1000
destination = 100000 #347991

matrix = [[0 for x in range(cols_count)] for x in range(rows_count)]

x = int(cols_count / 2) - 1
y = int(cols_count / 2) - 1
d = Direction.RIGHT
matrix[x][y] = 1
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

    matrix[x][y] = matrix[x-1][y+1] + matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y+1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1]
    if matrix[x][y] > 347991:
        break

    if d == Direction.RIGHT and matrix[x][y+1] == 0:
        d = Direction.UP
    elif d == Direction.UP and matrix[x-1][y] == 0:
        d = Direction.LEFT
    elif d == Direction.LEFT and matrix[x][y-1] == 0:
        d = Direction.DOWN
    elif d == Direction.DOWN and matrix[x+1][y] == 0:
        d = Direction.RIGHT

print(matrix[x][y])

# print('\n'.join([''.join(['{:4}'.format(item) for item in row])
#       for row in matrix]))
