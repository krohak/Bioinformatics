import random
from operator import mul
from functools import reduce
from bisect import bisect_left

# then, copy Pr, Normalize, and WeightedDie below this line
def Pr(Text, Profile):
    return reduce(mul, [ Profile[t][i] if t in Profile else 1 for i, t in enumerate(Text) ])

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