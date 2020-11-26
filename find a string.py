def count_substring(string, sub_string):
    str_len = len(string)
    sub_len = len(sub_string)
    count = 0
    for i in range(0, str_len):
        a = string.find(sub_string)
        if a > 0:
            string = string[a + 1:]
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)