def print_formatted(number):
    for i in range(1, number + 1):
        # o = oct(i)
        # o = o[o.find('o') + 1:]
        # h = hex(i)
        # h = list(c.upper() for c in h)
        # h = "".join(h)
        # h = h[h.find('X') + 1:]
        # b = bin(i)
        # b = b[b.find('b') + 1:]
        # print("{:d} {:s}".format(i, o))
        width = len("{0:b}".format(number))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)