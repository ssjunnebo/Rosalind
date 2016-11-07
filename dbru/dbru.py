from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def rev_comp(read):
    seq = Seq(read,IUPAC.unambiguous_dna)
    rev_seq = seq.reverse_complement()
    return(str(rev_seq))

def mk_set(seqs):
    S = set()
    for i in seqs:
        if i not in S:
            S.add(i)
        C = rev_comp(i)
        if C not in S:
            S.add(C)
    return(S)

data=[]
with open('rosalind_dbru.txt','r') as f:
    for line in f:
        data.append(line.strip())

s = mk_set(data)
for j in s:
    print("("+j[:-1]+", "+j[1:]+")")
