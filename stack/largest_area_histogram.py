heights = [2, 1, 5, 6, 2, 3]

stack = []
smallest_element_left_index = []
smallest_element_right_index = []


for i in range(0, len(heights)):
    while stack and stack[-1][0] >= heights[i]:
        stack.pop()

    if stack:
        smallest_element_left_index.append(stack[-1][1])

    else:
        smallest_element_left_index.append(-1)

    stack.append((heights[i], i))


while stack:
    stack.pop()


for i in range(len(heights) - 1, -1, -1):
    while stack and stack[-1][0] >= heights[i]:
        stack.pop()

    if stack:
        smallest_element_right_index.append(stack[-1][1])

    else:
        smallest_element_right_index.append(len(heights))

    stack.append((heights[i], i))

smallest_element_right_index.reverse()


res = 0
for i in range(0, len(heights)):
    val = smallest_element_right_index[i] - smallest_element_left_index[i] - 1
    res_new = heights[i] * val
    res = max(res, res_new)
print(res)
