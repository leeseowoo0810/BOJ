_ = int(input())
arr = list(map(int, input().split()))
maxValue = max(arr)
for i in range(len(arr)):
    arr[i] = (arr[i] / maxValue) * 100
print(sum(arr) / len(arr))