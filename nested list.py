def sortList(e):
    return e['score']


if __name__ == '__main__':
    mylist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append({"name": name,"score": score})
    mylist.sort(key=sortList)
    lowest = mylist[0]["score"]
    for student in mylist:
        if student["score"] == lowest:
            student["score"] = 0
    for student in mylist:
        if student["score"] != 0:
            second_lowest_score = student['score']
            break
    second_lowest_names = []
    for student in mylist:
        if student["score"] == second_lowest_score:
            second_lowest_names.append(student['name'])
    second_lowest_names.sort()
    for student in second_lowest_names:
        print(student, end=" ")



