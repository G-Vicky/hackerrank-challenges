def mutate_string(string, position, character):
    # mylist = list(string)                  1method using lists
    # mylist[position] = character
    # string = "".join(mylist)
    # return string
    return (string[:position] + character + string[position+1:])        # 2method using string slicing

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)