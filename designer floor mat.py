n,m = map(int, input().split())
string = "WELCOME"
org_design = ".|."
design = org_design
mid = n // 2
for i in range(0, n):
    if i < mid:
        print(design.center(m, "-"))
        design = org_design + design + org_design
    elif i == mid:
        print(string.center(m, "-"))
    else:
        design = design[:design.find(".|.")] + design[design.find(".|.") + 3:]
        design = design[:design.rfind(".|.")] + design[design.rfind(".|.") + 3:]
        print(design.center(m, "-"))
