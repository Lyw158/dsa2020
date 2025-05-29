t = int(input())
l = []
for i in range(t):
    n = int(input())
    l.append(list(input().split()))
flag = True
for i in range(t):
    queue = []
    flag = True
    for p in l[i]:
        if p[0] == '+':
            queue.append(int(p[1:]))
        elif p[0] == '-':
            if queue == [] or queue[0] != int(p[1:]):
                print('Case ' + str(i + 1) + ': no')
                flag = False
                break
            else:
                queue.pop(0)
    if flag:
        print('Case ' + str(i + 1) + ': yes')