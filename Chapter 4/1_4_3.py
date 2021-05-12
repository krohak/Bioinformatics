# first, import the random package
import random
from operator import mul
from functools import reduce
from bisect import bisect_left

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)

def GibbsSampler(Dna, k, t, N):
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs
    for _ in range(N):
        i = random.randint(0, t-1)
        Profile = ProfileWithPseudocounts(Motifs[:i]+Motifs[i+1:])
        Motifs[i] = ProfileGeneratedString(Motifs[i], Profile, k)
        BestScore, BestMotifs = min((Score(Motifs), Motifs), (Score(BestMotifs), BestMotifs))
    return BestMotifs 
        
# place all subroutines needed for GibbsSampler below this line
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

def Pr(Text, Profile):
    return reduce(mul, [ Profile[t][i] if t in Profile else 1 for i, t in enumerate(Text) ])

def ProfileMostProbableKmer(text, k, profile):
    probs = [ Pr(text[window:window+k], profile) for window in range(len(text)-k+1) ]
    idx = [ i for i, x in enumerate(probs) if x==max(probs) ][0]
    return text[idx:idx+k]

def Motifs(Profile, Dna, k):
    return [ ProfileMostProbableKmer(d, k, Profile) for d in Dna ]

def Normalize(Probabilities):
    return { k: p/sum(Probabilities.values()) for k, p in Probabilities.items() }

def WeightedDie(Probabilities):
    keys = list(Probabilities.keys())
    vals = list(Probabilities.values())
    cumm = [vals[0]]
    for i in range(1, len(vals)):
        cumm.append(vals[i]+cumm[-1])    
    idx = bisect_left(cumm, random.uniform(0,1))
    return keys[idx]

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}     
    for i in range(n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)  
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)