def day1_part1(directions):
    turn = 50
    ans = 0
    for d in directions:
        size = int(d[1:])
        if d[0] == 'R':
            turn += (size % 100)
        elif d[0] == 'L':
            turn -= (size % 100)
        turn = turn % 100
        if turn < 0:
            turn = 100 + turn
        if turn == 0:
            ans += 1
    return ans
def day1_part2(directions):
    turn = 50
    ans = 0
    for d in directions:
        size = int(d[1:])
        ans += size // 100
        old_turn = turn
        if d[0] == 'R':
            turn += (size % 100)
        elif d[0] == 'L':
            turn -= (size % 100)
        if (old_turn > 0 and turn <= 0) or (old_turn < 100 and turn >= 100):
            ans += 1
        turn = turn % 100
        if turn < 0:
            turn = 100 + turn
    return ans


if __name__ == "__main__":
    with open("day1data", "r") as f:
        data = [line.strip() for line in f.readlines()]
    
    print(day1_part1(data))
    print(day1_part2(data))