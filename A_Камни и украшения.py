from collections import Counter
J = input()
S = input()
count = Counter(S)
print(sum([S.count(key) for key in count if key in J]))
