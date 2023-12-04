a = [0, 1, 2, 3, 6, 5, 0, 1, 8, 5, 9]

stack = []
res = []

# loop through whole array


for i in range(len(a) - 1, -1, -1):
    while stack and stack[-1] >= a[i]:
        stack.pop()

    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)

    stack.append(a[i])


res.reverse()
print(res)
