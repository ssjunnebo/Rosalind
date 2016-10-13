from Bio import Phylo

#tree = Phylo.read('sampledata.txt','newick')
tree=Phylo.read('rosalind_ctbl.txt','newick')
taxa=[]
for c in tree.find_clades():
    if c.name:
        taxa.append(c.name)
taxa=sorted(taxa)


def color_clade(clade, root):
    for subclade in clade.clades:
        if not subclade.is_terminal():
            print_subtrees(subclade, root)
            color_clade(subclade, root)

def print_subtrees(clade, root):
    array=''
    all_nodes = set(root.get_terminals())
    colored_nodes = set(clade.get_terminals())
    noncolored_nodes = all_nodes - colored_nodes
    on_tree=[]
    off_tree=[]
    for i in colored_nodes:
        on_tree.append(i.name)
    for j in noncolored_nodes:
        off_tree.append(j.name)
    for taxon in taxa:
        if taxon in on_tree:
            array+='1'
        elif taxon in off_tree:
            array+='0'
    print(array)

root = tree.root
color_clade(root, root)
