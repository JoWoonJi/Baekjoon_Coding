x=[]
for i in range(10):
    n=int(input())
    x.append(n%42)
print(len(set(x)))