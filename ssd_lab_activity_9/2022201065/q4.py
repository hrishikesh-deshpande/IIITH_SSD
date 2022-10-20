ip = input()
k = int(input())

f = {}
  
for i in ip:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

print(len(f))

for i in range(len(ip)-k+1):
    l = [ip[i] for i in range(i,i+k)]
    f = {}
    for i in l:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    print(len(f))