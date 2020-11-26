# print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6] ])

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylist = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    result = []
    for item in mylist:
        tot = 0
        for a in item:
            tot += a
        if tot != n:
            result.append(item)
    print(result)