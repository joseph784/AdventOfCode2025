from functools import reduce
import collections


def get_factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def day2_part1(ranges):
    range_array = []
    ranges = ranges[0].split(",")
    for range1 in ranges:
        parts = range1.split("-")
        range_array.append((int(parts[0]), int(parts[1])))
    range_array.sort()
    ans = 0
    for start, end in range_array:
        for i in range(start, end + 1):
            s = str(i)
            n = len(s)
            if n % 2 == 1:
                continue
            
            if s[: n//2] == s[n//2:]:
                ans += i
    return ans

def day2_part2(ranges):
    factors = collections.defaultdict()
    range_array = []
    ranges = ranges[0].split(",")
    for range1 in ranges:
        parts = range1.split("-")
        range_array.append((int(parts[0]), int(parts[1])))
    range_array.sort()
    ans = 0
    for start, end in range_array:
        for i in range(start, end + 1):
            s = str(i)
            n = len(s)
            if n not in factors:
                factors[n] = get_factors(n)
            f = factors[n]
            for factor in f:
                if factor == n:
                    continue
                invalid = True
                for j in range(n // factor):
                    if s[j * factor: (j + 1) * factor] != s[0:factor]:
                        invalid = False
                        break
                if invalid:
                    ans += i
                    break
    return ans








if __name__ == "__main__":
    # print(factors(11))
    with open("day2data", "r") as f:
        data = [line.strip() for line in f.readlines()]
    
    # print(day2_part1(data))
    print(day2_part2(data))