art=int(input())
eng=list(map(int,input().split()))
med=0
for i in range(0,art):
  for j in range(0,i):
    if(eng[j]<eng[i]):
      med=med+eng[j]
print(med)
