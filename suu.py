a,b=map(int,input().split())
cnt=0
arr=list()
for _ in range(a+1,b):
    cnt+=1
    arr.append(_)
print(cnt)
print(arr)
