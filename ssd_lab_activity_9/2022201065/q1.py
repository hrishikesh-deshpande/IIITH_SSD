t = input()
ip = input()
l = ip.split(' ')
l = [int(i) for i in l]
print(sum(l))
print(str(min(l))+' '+str(max(l)))