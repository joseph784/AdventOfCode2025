import os

def day4_part1(data):
    grid = []
    ans = 0
    for line in data:
        row = [x for x in line]
        grid.append(row)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                if check(i,j, grid):
                    ans += 1
    return ans

def check(i,j, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    access = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '@':
            access += 1
    return access < 4

def day4_part2(data):
    grid = []
    ans, prev = 0, -1
    for line in data:
        row = [x for x in line]
        grid.append(row)
    while ans != prev:
        prev = ans
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    if check(i,j, grid):
                        ans += 1
                        grid[i][j] = '.'
    return ans



if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "day4data"), "r") as f:
        data = [line.strip() for line in f.readlines()]
    print(day4_part1(data))
    print(day4_part2(data))