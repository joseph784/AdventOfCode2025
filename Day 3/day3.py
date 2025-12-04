import os

def day3_part1(data):
    ans = 0
    for line in data:
        one, ten = 0, 0
        i,j = 0,0
        line = str(line)
        while i < (len(line) - 1):
            if ten < int(line[i]):
                j = i + 1
                ten = int(line[i])
            i += 1
        while j < (len(line)):
            one = max(one, int(line[j]))
            j += 1
        ans += (ten * 10) + one        
    return ans

def day3_part2(data):
    ans = 0
    for line in data:
        mult = 100000000000
        i, j, k = 11, 0, 0
        max = 0
        while i > -1:
            while j < len(line) - i:
                if int(line[j]) > max:
                    max = int(line[j])
                    k = j + 1
                j += 1
            ans += max * mult
            mult = mult // 10
            max = 0
            j = k
            i -= 1
    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "day3data"), "r") as f:
        data = [line.strip() for line in f.readlines()]
    print(day3_part1(data))
    print(day3_part2(data))