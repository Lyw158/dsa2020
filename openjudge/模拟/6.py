def max_submatrix_sum(matrix, n):
    max_sum = float('-inf')

    for top in range(n):
        col_sums = [0] * n
        for bottom in range(top, n):
            for col in range(n):
                col_sums[col] += matrix[bottom][col]
            current_sum = 0
            min_prefix = 0
            for val in col_sums:
                current_sum += val
                if current_sum - min_prefix > max_sum:
                    max_sum = current_sum - min_prefix
                if current_sum < min_prefix:
                    min_prefix = current_sum

    return max_sum

import sys
input_lines = [line.strip() for line in sys.stdin if line.strip()]
input_lines = ' '.join(input_lines)
input_lines = input_lines.split()
idx = 0
n = int(input_lines[idx])
idx += 1
m = []
for i in range(n):
    m.append([int(x) for x in input_lines[idx:idx+n]])
    idx += n

print(max_submatrix_sum(m, n))