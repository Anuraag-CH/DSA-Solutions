def reverse_stack(stack):
    if stack.is_empty():
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.push(top)

#space complexity: O(n)
#time complexity: O(n^2)