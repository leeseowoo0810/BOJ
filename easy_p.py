n=int(input())
arr=[]
for i in range(n):
    arr.append(input().split())
arr=sorted(arr,key= lambda  x:x[1])
print(tmp[0][0])