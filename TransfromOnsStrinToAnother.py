#Transform One String to Another using Minimum Number of Given Operation:

def transformString(A, B):
    if len(A) != len(B):
        return -1   
     
    count = 0
    i = len(A) - 1
    j = len(B) - 1
    
    while i >= 0 and j >= 0:
        if A[i] == B[j]:
            i -= 1
            j -= 1
        else:
            count += 1
            i -= 1    
    return count

A = "EACBD"
B = "EABCD"
print("Operations Required: ", transformString(A, B))

