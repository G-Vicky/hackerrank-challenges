if __name__ == '__main__':
    s = input()
    isalnum = isalpha = isdigit = islower = isupper = False
    for c in s:
        if c.isalnum() and not isalnum:
            isalnum = True
        if c.isalpha() and not isalpha:
            isalpha = True
        if c.isdigit() and not isdigit:
            isdigit = True
        if c.islower() and not islower:
            islower = True
        if c.isupper() and not isupper:
            isupper = True

    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(islower)
    print(isupper)