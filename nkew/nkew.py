import sys
from Bio import Phylo
import io

f=open('rosalind_nkew.txt','r')
pairs=[i.split('\n') for i in f.read().strip().split('\n\n')]

for i, line in pairs:
    x,y=line.split()
    tree=Phylo.read(io.StringIO(i),'newick')
    sys.stdout.write('%s' % round(tree.distance(x,y))+' ')
sys.stdout.write('\n')
