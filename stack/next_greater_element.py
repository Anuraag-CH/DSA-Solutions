a = [1, 5, 6, 6, 7, 3, 4, 12, 19, 0, 1]

stack = []

res = []

# loop over every element
for i in range(len(a) - 1, -1, -1):
    # check if stack is empty and check top element
    while stack and stack[-1] <= a[i]:
        stack.pop()

    # if element is greater add to result else pop
    if stack:
        res.append(stack[-1])
    else:
        res.append(-1)

    stack.append(a[i])

res.reverse()
print(res)
