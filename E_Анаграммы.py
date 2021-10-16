from collections import Counter
first_line = input()
second_line = input()
print(int(Counter(first_line) == Counter(second_line)))
