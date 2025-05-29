r, c, s = input().split(maxsplit=2)
r, c = int(r), int(c)
l = [['0' for _ in range(c)] for _ in range(r)]
def f(s):
    ans = []
    for i in s:
        if i == ' ':
            ans.append('00000')
            continue
        ans.append(format(ord(i) - ord('A') + 1, '05b'))
    return ''.join(ans)

def write(s, l):
    i = 0
    l1 = [[0 for _ in range(c)] for _ in range(r)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0 
    p, q = 0, 0
    while i < len(s):
        l[p][q] = s[i]
        l1[p][q] = 1
        next_p, next_q = p + directions[direction_index][0], q + directions[direction_index][1]
        if 0 <= next_p < r and 0 <= next_q < c and l1[next_p][next_q] == 0:
            p, q = next_p, next_q
            i += 1
        else:
            direction_index = (direction_index + 1) % 4
            p, q = p + directions[direction_index][0], q + directions[direction_index][1]
            i += 1
    return ''.join([''.join(l[i]) for i in range(r)])
print(write(f(s), l))
