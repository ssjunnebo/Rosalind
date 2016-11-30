mass_table = {'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841,'G':57.02146,'H':137.05891,'I':113.08406,'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276,'Q':128.05858,'R':156.10111,'S':87.03203,'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06333}

def weight(s):
    w = 0
    for aa in s:
        w += mass_table.get(aa)
    return round(w, 5)

def multiplicity(p):
    m = 0
    for i in range(len(p) + 1):
        prefix = p[0: i]
        suffix = p[-1: i: -1]
        if weight(prefix) in masses or weight(suffix) in masses:
            m += 1
    return m

with open('rosalind_prsm.txt', 'r') as f:
    n = int(f.readline())
    pdb = []
    for i in range(n):
        pdb.append(f.readline().strip())
    masses = set([round(float(j), 5) for j in f.readlines()])

mult = 0
for prt in pdb:
    m = multiplicity(prt)
    if m > mult:
        mult = m
        prot = prt
print(mult)
print(prot)
