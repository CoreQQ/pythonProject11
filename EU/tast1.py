#Знайди перше непослідовне число:

def search(arr):
    i = arr[0]
    for x in arr:
        if x != i:
            return x - 1
            break
        i += 1

arr = [1, 2, 3, 4, 6, 7, 8]
print(search(arr))