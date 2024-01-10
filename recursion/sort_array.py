def sort_array(arr):
    if len(arr) == 0 :
        return 
    temp = arr.pop()
    sort_array(arr)
    insert(arr, temp)

def insert(arr, temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    val = arr.pop()
    insert(arr, temp)
    arr.append(val)

arr = [1, 20, 31, -4, 5]
sort_array(arr)
print(arr)
#space complexity: O(n)
#time complexity: O(n^2)
    