n = int(input())
el_to_compare = '1'
for _ in range(n):
    i = int(input())
    if i == el_to_compare:
        continue
    else:
        el_to_compare = i
        print(i)
