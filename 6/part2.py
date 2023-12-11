import sys


def solve(total_time, max_distance):
    num_wins = 0
    for i in range(total_time + 1):
        speed = i
        time = total_time - i
        distance = speed * time

        if distance > max_distance:
            num_wins += 1

    return num_wins

with open(sys.argv[1]) as f:
    time = int(''.join(t.strip() for t in f.readline().split(':')[1].split()))
    distance = int(''.join(d.strip() for d in f.readline().split(':')[1].split()))

print(solve(time, distance))

