from collections import defaultdict

def CountWithPseudocounts(Motifs):    
    m, n = len(Motifs), len(Motifs[0])
    count = defaultdict(lambda: [1]*n)    
    for j in range(n):
        for i in range(m):
            count[Motifs[i][j]][j]+=1
    return dict(count)