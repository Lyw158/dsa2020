def get_priority(i, j, s):
    t = 4
    index = i
    while index < j + 1:
        if s[index] == '(':
            while index < j + 1 and s[index] != ')':
                index += 1
        if s[index] == '+':
            t = min(t, 1)
        elif s[index] == '*':
            t = min(t, 2)
        index += 1
    return t

def remove_redundant_brackets(s):

    stack = []
    pairs = []  # 存储括号对
    priority = {'+': 1, '*': 2}
    s = list(s)
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                left = stack.pop()
                pairs.append((left, i))
    
    remove = set()
    for l, r in pairs:
        i, j = l, r
        while i >= 0 and j < len(s) and s[i] == '(' and s[j] == ')':
            i -= 1 
            j += 1
        left_char = s[i] if i >= 0 else None
        right_char = s[j] if j < len(s) else None
        min_prio = get_priority(l+1, r-1, s)
        if min_prio == 4:
            remove.add(l)
            remove.add(r)
            continue
        if (left_char == '*' and min_prio < 2) or \
           (right_char and priority.get(right_char, 0) > min_prio):
            continue
        remove.add(l)
        remove.add(r)
    
    # 步骤3：构建结果字符串
    return ''.join(s[i] for i in range(len(s)) if i not in remove)

import sys
lines = sys.stdin.read().strip().split('\n')
ans = []
for line in lines:
    ans.append(remove_redundant_brackets(line))
for i in ans:
    print(i)
