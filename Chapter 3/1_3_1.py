from collections import defaultdict
def Count(Motifs):    
    m, n = len(Motifs), len(Motifs[0])
    count = defaultdict(lambda: [0]*n)    
    for j in range(n):
        for i in range(m):
            count[Motifs[i][j]][j]+=1
    return dict(count)

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    countMatrix = Count(Motifs)
    profile = { k: [ x/t for x in arr ] for k, arr in countMatrix.items() }
    return profile