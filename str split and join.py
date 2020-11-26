def split_and_join(line):
    splitted = line.split(" ")
    print(splitted)
    hypenated = "-".join(splitted)
    return hypenated

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)