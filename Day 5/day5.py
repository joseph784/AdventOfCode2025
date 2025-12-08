import os

def day5_part1(data):
    i = 0
    ranges = []
    while i < len(data):
        if data[i] == '':
            break
        parts = data[i].split("-")
        ranges.append((int(parts[0]), int(parts[1])))
        i += 1
    ans = 0
    i += 1
    while i < len(data):
        line = data[i]
        for start, end in ranges:
            if start <= int(line) <= end:
                ans += 1
                break
        i += 1
    return ans

def day5_part2(data):
    i = 0
    ranges = []
    while i < len(data):
        if data[i] == '':
            break
        parts = data[i].split("-")
        ranges.append((int(parts[0]), int(parts[1])))
        i += 1
    ranges.sort()
    merged_ranges = [ranges[0]]
    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        if current_start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            merged_ranges.append((current_start, current_end))
    ans = 0
    for start, end in merged_ranges:
        ans += (end - start + 1)
    return ans

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "day5data"), "r") as f:
        data = [line.strip() for line in f.readlines()]
    
    #print(day5_part1(data))
    print(day5_part2(data))