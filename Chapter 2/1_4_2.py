# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    
    runningMin = float('inf')
    minIndices = []
    
    prev = 0
    for i in range(1, len(Genome)+1):
        curr = prev
        if Genome[i-1]=='G':
            curr+=1 
        elif Genome[i-1]=='C':
            curr-=1
        
        if curr == runningMin:
            minIndices.append(i)
            
        elif curr < runningMin:
            minIndices = []
            minIndices.append(i)
            runningMin = curr
            
        prev = curr
            
    return minIndices
    