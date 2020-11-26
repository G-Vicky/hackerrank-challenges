if __name__ == '__main__':
    N = int(input())
    mylist = []
    for i in range(1, N+1):
        command, *value = input().split()
        if command == "append":
            mylist.append(int(value[0]))
        elif command == "insert":
            mylist.insert(int(value[0]), int(value[1]))
        elif command == "remove":
            mylist.remove(int(value[0]))
        elif command == "pop":
            mylist.pop()
        elif command == "sort":
            mylist.sort()
        elif command == "reverse":
            mylist.reverse()
        elif command == "print":
            print(mylist)