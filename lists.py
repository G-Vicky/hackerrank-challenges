if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = list(arr)
    winner = max(mylist)
    while max(mylist) == winner:
        mylist.remove(winner)
    mylist.sort()
    print(mylist.pop())


