from itertools import product

def quartet(R):
    A = []
    B = []
    for i in range(len(R)):
        if R[i] == '0':
            A.append(species[i])
        elif R[i] == '1':
            B.append(species[i])
    if len(A) > 1 and len(B) > 1:
        A_pairs = [(A[i], A[j]) for i in range(len(A)) for j in range(i+1, len(A))]
        B_pairs = [(B[i], B[j]) for i in range(len(B)) for j in range(i+1, len(B))]
        for pair in product(A_pairs, B_pairs):
            Q.add(frozenset(map(frozenset, pair)))
    return


with open('rosalind_qrt.txt', 'r') as f:
    species = f.readline().strip('\n').split(' ')
    C = f.read().splitlines()

Q = set()
for row in C:
    q = quartet(row)

for ((a,b),(c,d)) in Q:
    print('{%s, %s} {%s, %s}' % (a,b,c,d))
