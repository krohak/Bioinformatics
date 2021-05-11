from operator import mul
from functools import reduce

def CountWithPseudocounts(Motifs):    
    m, n = len(Motifs), len(Motifs[0])
    count = {}
    for char in 'ATCG': count[char]=[1]*n
    for j in range(n):
        for i in range(m):
            count[Motifs[i][j]][j]+=1
    return dict(count)

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    countMatrix = CountWithPseudocounts(Motifs)
    profile = { k: [ x/(t+4) for x in arr ] for k, arr in countMatrix.items() }
    return profile

def Consensus(Motifs):
    countMatrix = CountWithPseudocounts(Motifs)
    highestF = map((lambda arr: [i for i, x in enumerate(arr) if x==max(arr)][-1]), zip(*countMatrix.values()))
    keys = list(countMatrix.keys())
    return ''.join([ keys[f] for f in list(highestF) ])

def Score(Motifs):
    consensus = Consensus(Motifs)    
    return sum(map(lambda arr: sum([ 1 for i, s in enumerate(arr) if s!=consensus[i] ]), Motifs))

# Then copy your ProfileMostProbableKmer(Text, k, Profile) and Pr(Text, Profile) functions here.
def Pr(Text, Profile):
    return reduce(mul, [ Profile[t][i] if t in Profile else 1 for i, t in enumerate(Text) ])

def ProfileMostProbableKmer(text, k, profile):
    probs = [ Pr(text[window:window+k], profile) for window in range(len(text)-k+1) ]
    idx = [ i for i, x in enumerate(probs) if x==max(probs) ][0]
    return text[idx:idx+k]

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
        
    n = len(Dna[0])
    for win in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][win:win+k])
        for i in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:i])
            #print(win, i, "ProfileWithPseudocounts", Motifs[0:i], P)
            m = ProfileMostProbableKmer(Dna[i], k, P)
            #print(win, i, "ProfileMostProbableKmer", Dna[i], m)
            Motifs.append(m)            
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs