import os
def day6_part1(data):
    totals = [0] * 10000
    ops = []
    for operation in data[-1]:
        if operation not in ["+", "*"]:
            continue
        ops.append(operation)
    for i in range(len(data) - 1):
        values = data[i].split(" ")
        j = 0
        for num in values:
            if not num.isdigit():
                continue
            val = int(num)
            if ops[j] == "+":
                totals[j] += val
            elif ops[j] == "*":
                if totals[j] == 0:
                    totals[j] = 1
                totals[j] *= val
            j += 1
    ans = 0
    for total in totals:
        ans += total 
    return ans

def day6_part2(data):
    totals = [0] * 10000
    ops = []
    for operation in data[-1]:
        if operation not in ["+", "*"]:
            continue
        ops.append(operation)
    ops.append("END")
    opCount = len(ops) - 1
    for j in range(len(data[0]) - 1, -1 ,-1):
        digits = []
        for i in range(len(data) -1): 
            if data[i][j].isdigit():
                digits.append(int(data[i][j]))
        mult = 10**(len(digits) - 1)
        num = 0
        for digit in digits:
            num += digit * mult
            mult //= 10
        operation = ops[opCount]
        if operation == "+": 
            totals[opCount] += num
        elif operation == "*" and num != 0:
            if totals[opCount] == 0:
                totals[opCount] = 1
            totals[opCount] *= num
        if len(digits) == 0:
            opCount -= 1
    ans = 0
    for i in totals:
        ans += i
    return ans

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "day6data"), "r") as f:
        data = f.readlines()
    print(day6_part1(data))
    print(day6_part2(data))