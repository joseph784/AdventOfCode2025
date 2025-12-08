import os
import heapq
import collections
import math

def day8_part1(data):
    circuits = collections.defaultdict(set)
    nodes = {}
    q = []
    for i in range(len(data)):
        nodes[i] = i
        i_parts = [int(x) for x in data[i].split(",")]
        circuits[i].add(i)
        for j in range(i + 1, len(data)):
            j_parts = [int(x) for x in data[j].split(",")]
            distance = math.sqrt((i_parts[0] - j_parts[0])**2 + (i_parts[1] - j_parts[1])**2 + (i_parts[2] - j_parts[2])**2)
            heapq.heappush(q, (distance, i, j))
    i = 0
    while i < 1000:
        distance, a, b = heapq.heappop(q)
        circuits_a = nodes[a]
        circuits_b = nodes[b]
        if circuits_a != circuits_b:
            for val in circuits[circuits_b]:
                circuits[circuits_a].add(val)
                nodes[val] = circuits_a
            del circuits[circuits_b]
        i += 1
    circuitsQ = []
    ans = 1
    for key, val in circuits.items():
        heapq.heappush(circuitsQ, (-len(val), key))
    for _ in range(3):
        size, key = heapq.heappop(circuitsQ)
        ans *= -size
    return ans


def day8_part2(data):

    circuits = collections.defaultdict(set)
    nodes = {}
    q = []
    for i in range(len(data)):
        nodes[i] = i
        i_parts = [int(x) for x in data[i].split(",")]
        circuits[i].add(i)
        for j in range(i + 1, len(data)):
            j_parts = [int(x) for x in data[j].split(",")]
            distance = math.sqrt((i_parts[0] - j_parts[0])**2 + (i_parts[1] - j_parts[1])**2 + (i_parts[2] - j_parts[2])**2)
            heapq.heappush(q, (distance, i, j))
    lastA, lastB = -1, -1
    while len(circuits) > 1:
        distance, a, b = heapq.heappop(q)
        lastA, lastB = a, b
        circuits_a = nodes[a]
        circuits_b = nodes[b]
        if circuits_a != circuits_b:
            for val in circuits[circuits_b]:
                circuits[circuits_a].add(val)
                nodes[val] = circuits_a
            del circuits[circuits_b]
        i += 1
    a_parts = [int(x) for x in data[lastA].split(",")]
    b_parts = [int(x) for x in data[lastB].split(",")]
    return a_parts[0] * b_parts[0]


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, "day8data"), "r") as f:
        data = [line.strip() for line in f.readlines()]
    #print(day8_part1(data))
    print(day8_part2(data))
