ip = input()
f = {}
  
for i in ip:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

f = sorted(f.items(), key=lambda x: (-x[1], x[0]))

print(str(f[0][0])+' '+str(f[1][0]))