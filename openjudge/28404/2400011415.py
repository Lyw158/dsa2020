n = int(input())
d = {}
for i in range(n):
    customer, table, food = list(input().strip().split(','))
    if table not in d.keys():
        d[table] = {}
    
    if food not in d[table].keys():
        d[table][food] = 1
    else:
        d[table][food] += 1
foods = sorted(set(food_item for table in d.values() for food_item in table.keys()))
header = ['Table'] + foods
ans = []
for table in sorted(d.keys(), key=int):
    row = [table]
    for food in foods:
        row.append(str(d[table].get(food, 0)))
    ans.append(row)

out = []
out.append("\t".join(map(str, header)))
for row in ans:
    out.append("\t".join(map(str, row)))
print("\n\n".join(out))
print(d)