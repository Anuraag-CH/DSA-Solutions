def check(length, string):
    count_0 = 0
    count_1 = 0
    possible_0 = 0
    for i in range(length - 1):
        if string[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

        if string[i] != string[i + 1]:
            possible_0 += 1

    if string[length - 1] == "0":
        count_0 += 1
    else:
        count_1 += 1

    if (count_0 + possible_0) >= count_1:
        return "YES"
    else:
        return "NO"


test_cases = int(input())


for i in range(test_cases):
    length = int(input())
    string = input()

    if length == 1:
        if string[0] == "0":
            print("YES")
        else:
            print("NO")

    else:
        print(check(length, string))
