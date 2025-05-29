s = list(input().split())[::-1]
stack = []
for i in s:
    if i in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(b - a)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(b / a)
    else:
        stack.append(float(i))
print(f'{stack[0]:.1f}')