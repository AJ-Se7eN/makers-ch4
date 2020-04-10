numbers = input().split()
new=[]
for i in numbers:
    new.append(int(i))
a=1
for i in new:
    if i == a:
        a+=1
print(a)