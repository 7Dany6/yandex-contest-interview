n = int(input())


def generate(current, opening, closing, n):
    if len(current) == n * 2:
        print(current)
        return
    if opening < n:
        generate(current+"(", opening+1, closing, n)
    if closing < opening:
        generate(current+")", opening, closing+1, n)


generate('', 0, 0, n)
