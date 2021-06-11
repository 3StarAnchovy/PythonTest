score = list(map(int, input().split()))
sum = 0
for i in score:
    sum += i
avg = sum/len(score)
print(int(avg))

#print(sum(score)/len(score))