n = int(input())
s = []
for i in range(n):
    s1, s2, s3 = list(input().split())
    s.append([s1, s2, s3])

def find_solution(s1, s2, s3):
    if len(s3) > len(s1) + 1 and len(s3) > len(s2) + 1:
        return 'No Solution'
    if len(s3) < len(s1) or len(s3) < len(s2):
        return 'No Solution'
    from itertools import permutations
    letters = sorted(list(set(s1 + s2 + s3)))
    for digits in permutations('0123456789', len(letters)):
        assignment = {letters[i]: digits[i] for i in range(len(letters))}
        if is_valid(assignment, s1, s2, s3):
            num1 = ''.join([assignment[c] for c in s1])
            num2 = ''.join([assignment[c] for c in s2])
            num3 = ''.join([assignment[c] for c in s3])
            return f"{num1}+{num2}={num3}"
    return "No Solution"
    
def is_valid(assignment, s1, s2, s3):
    if assignment[s1[0]] == '0' or assignment[s2[0]] == '0' or assignment[s3[0]] == '0':
        return False
    num1 = int(''.join([assignment[c] for c in s1]))
    num2 = int(''.join([assignment[c] for c in s2]))
    num3 = int(''.join([assignment[c] for c in s3]))
    return num1 + num2 == num3

for p in s:
    print(find_solution(p[0], p[1], p[2]))