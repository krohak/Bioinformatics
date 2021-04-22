# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    # your code here
    skew = [ 0 for _ in range(len(Genome)+1) ]
    skew[0] = 0
    
    for i in range(1, len(Genome)+1):
        skew[i] = skew[i-1]
        if Genome[i-1]=='G':
            skew[i]+=1 
        elif Genome[i-1]=='C':
            skew[i]-=1
    return skew