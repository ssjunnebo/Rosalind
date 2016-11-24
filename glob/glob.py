from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62

seqs = []
with open('rosalind_glob.fasta','r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        seqs.append(record.seq)
s = seqs[0]
t = seqs[1]
alignments = pairwise2.align.globalds(s, t, blosum62, -5, -5)
print(pairwise2.format_alignment(*alignments[0]))
