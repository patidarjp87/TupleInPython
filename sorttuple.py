print('program to sort tuple elements \n Enter a tuple')
p=eval(input())
i=0
while i!=len(p)-1:
    if p[i]>p[i+1]:
        t=p[i]
        p[i]=p[i+1]
        p[i+1]=t
        i+=1
else:
    print('sorted tuple is',p)
input()