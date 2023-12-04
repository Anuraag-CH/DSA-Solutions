a = [0, 1, 2, 3, 6, 5, 0, 1, 8, 5, 9]

stack = []
res = []

# loop through whole array


for i in range(0, len(a)):
    while stack and stack[-1] >= a[i]:
        stack.pop()

    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)

    stack.append(a[i])


print(res)
