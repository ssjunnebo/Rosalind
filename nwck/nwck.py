import sys
from Bio import Phylo
import io

#open file and parse data
f = open('rosalind_nwck.txt','r')
pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]

#for each pair:
#-parse data further with biopython
#-add branch length 1 to all branches
#-use bioputhons Phylo distance funktion to get distances
#-print result on requested format

for i, line in pairs:
    x,y = line.split()
    tree = Phylo.read(io.StringIO(i),'newick')
    clades = tree.find_clades()
    for clade in clades:
        clade.branch_length = 1
    sys.stdout.write('%s' % tree.distance(x,y) + ' ')
sys.stdout.write('\n')
