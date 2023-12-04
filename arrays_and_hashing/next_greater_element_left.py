a = [2, 3, 6, 4, 3, 3, 6, 7]

stack = []
res = []


for i in range(0, len(a)):
    while stack and stack[-1] <= a[i]:
        stack.pop()

    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)

    stack.append(a[i])

print(res)
