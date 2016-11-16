A=[]
with open('rosalind_afrq.txt','r') as f:
    for nr in f.readline().split(' '):
        A.append(float(nr))

for i in A:
    print(round(2*i**0.5-i,3),end=' ')
