import os
import collections

def day7_part1(data):
    ans = 0
    beams = set()
    for line in data:
        for i in range(len(line)):
            if line[i] == "S":
                beams.add(i)
            if line[i] == "^":
                if i in beams:
                    ans += 1
                    beams.remove(i)
                    beams.add(i + 1)
                    beams.add(i - 1)
    return ans

def day7_part2(data):
    beams = collections.defaultdict(lambda: 0)
    for line in data:
        for i in range(len(line)):
            if line[i] == "S":
                beams[i] += 1
            if line[i] == "^":
                beams[i+1] += beams[i]
                beams[i-1] += beams[i]
                beams[i] = 0 
    ans = 0
    for key, val in beams.items():
        if val > 0:
            ans += val
    return ans
if __name__ == '__main__':
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "day7data"), "r") as f:
        data = [line.strip() for line in f.readlines()]
    print(day7_part1(data))
    print(day7_part2(data))