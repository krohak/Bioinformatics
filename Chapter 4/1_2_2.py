# import the random package here
import random
from operator import mul
from functools import reduce

# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna, k)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
def RandomMotifs(Dna, k, t):
    M = len(Dna[0])-k
    return [ d[random.randint(0, M):][:k] for d in Dna ]

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

def Motifs(Profile, Dna, k):
    return [ ProfileMostProbableKmer(d, k, Profile) for d in Dna ]

def Pr(Text, Profile):
    return reduce(mul, [ Profile[t][i] if t in Profile else 1 for i, t in enumerate(Text) ])

def ProfileMostProbableKmer(text, k, profile):
    probs = [ Pr(text[window:window+k], profile) for window in range(len(text)-k+1) ]
    idx = [ i for i, x in enumerate(probs) if x==max(probs) ][0]
    return text[idx:idx+k]