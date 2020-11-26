def print_rangoli(size):
    n = size
    width = n + (n - 1) + (n*2 - 2)
    alphabets = [chr(c) for c in range(97, 97+n)]
    rangoli = []
    design = []
    for i in range(0, n):
        rangoli.append(alphabets[i:])
    for alphas in rangoli:
        ralphas = alphas.copy()
        ralphas.reverse()
        ran = ralphas[:] + alphas[1:]
        design.append(ran)

    mid = n // 2
    design.reverse()
    for d in design:
        text = "-".join(d)
        print(text.center(width, "-"))
    design.pop()
    design.reverse()
    for d in design:
        text = "-".join(d)
        print(text.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
