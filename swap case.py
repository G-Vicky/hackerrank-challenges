def swap_case(s):
    mystr = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                c = c.lower()
            else:
                c = c.upper()
        mystr += c
    return mystr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)