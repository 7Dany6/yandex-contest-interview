n = int(input())
sequence = []
for _ in range(n):
    sequence.append(int(input()))
sequence.append("A")
count = 0
results = []
for i in range(len(sequence)):
    if sequence[i] == 1:
        count += 1
    else:
        results.append(count)
        count = 0
print(max(results))
