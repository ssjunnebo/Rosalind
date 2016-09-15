def lcs(s,t):
    lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
    spliced_motif = ''
    x, y = len(s), len(t)
    while x * y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            spliced_motif = s[x - 1] + spliced_motif
            x -= 1
            y -= 1
    return(spliced_motif)


def scs(s,t):
    subseq = lcs(s,t)
    superseq = ''
    i, j = 0, 0
    for nt in subseq:
        if i < len(s):
            while s[i] != nt:
                superseq += s[i]
                i += 1
            i += 1
        if j < len(t):
            while t[j] != nt:
                superseq += t[j]
                j += 1
            j += 1
        superseq += nt
    if i < len(s):
        superseq += s[i:]
    if j < len(t):
        superseq += t[j:]
    return(superseq)

s, t = [line.strip() for line in open('rosalind_scsp.txt','r')]
print(scs(s,t))
