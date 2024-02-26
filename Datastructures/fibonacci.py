length=int(input('Enter the length'))
seq=[]
n1=0
n2=1
count=0
if length<=0:
    print('please enter the valid length')
elif length==1:
    seq.append(n1)
    print(seq)
else:
    while count<=length:
        seq.append(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count +=1
    print(seq)
        