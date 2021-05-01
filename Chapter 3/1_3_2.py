from collections import defaultdict
def Count(Motifs):    
    m, n = len(Motifs), len(Motifs[0])
    count = defaultdict(lambda: [0]*n)    
    for j in range(n):
        for i in range(m):
            count[Motifs[i][j]][j]+=1
    return dict(count)

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    countMatrix = Count(Motifs)
    highestF = map((lambda arr: [i for i, x in enumerate(arr) if x==max(arr)][-1]), zip(*countMatrix.values()))
    keys = list(countMatrix.keys())
    return ''.join([ keys[f] for f in list(highestF) ])

def Score(Motifs):
    consensus = Consensus(Motifs)    
    return sum(map(lambda arr: sum([ 1 for i, s in enumerate(arr) if s!=consensus[i] ]), Motifs))