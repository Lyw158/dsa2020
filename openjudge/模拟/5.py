n = int(input())

def cantor(n):
    if n == 1:
        return '*-*'
    return cantor(n - 1) + '-' * (3 ** (n - 1)) + cantor(n - 1)

print(cantor(n))