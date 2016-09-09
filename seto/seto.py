#read file and format data into sets of integers
data = []
with open('rosalind_seto.txt','r') as f:
    for line in f:
        data.append(line.strip('\n'))
U = set(range(1,int(data[0])+1))
A = set([int(x) for x in data[1].strip('{}').split(',')])
B = set([int(x) for x in data[2].strip('{}').split(',')])

#perform set operations
union = A.union(B)
intersection = set(A).intersection(B)
diff_AB = A-B
diff_BA = B-A
A_comp = U-A
B_comp = U-B

#print answers
print(union)
print(intersection)
print(diff_AB)
print(diff_BA)
print(A_comp)
print(B_comp)
