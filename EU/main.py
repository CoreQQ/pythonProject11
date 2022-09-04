def reverse(num):
    if num <= 0:
        return num
    else:
        return num * -1


num = int(input("Enter num: "))
print(reverse(num))