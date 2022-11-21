names={}
n=int(input('Enter number of names'))
for i in  range(n):
    names[i+1]=input('Enteraname')
name=list(names.values())
pos=int(input('Enterposition'))
name.sort(key=lambda x:x[pos])
print(name)
