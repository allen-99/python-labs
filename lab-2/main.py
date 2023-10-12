n = int(input())
arr = []
tmp = 1
i = 2
while tmp <= n:
    arr.append(tmp)
    tmp += i
    i += 1

count = 0
ymp = 1
while n > 0:
    if arr[len(arr) - ymp] <= n:
        count += 1
        print(arr[len(arr) - ymp])
        n -= arr[len(arr) - ymp]
    else:
        ymp += 1

print(arr)
print(count)
