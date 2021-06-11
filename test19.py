num = list(map(int,input().split()))
sum =num[0]
for i in range(1,num[1]):
    sum*=num[0]
print(sum)