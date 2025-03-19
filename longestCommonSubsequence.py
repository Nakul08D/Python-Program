# Longest Common Subsequence String(LCS):

def lcs(s1, s2, l1, l2):

    if(l1==0 or l2==0):
        return 0
    elif(s1[l1-1]==s2[l2-1]):
        return 1+(lcs(s1, s2, l1-1, l2-1))
    else:
        return max(lcs(s1, s2, l1-1, l2), lcs(s1, s2, l1, l2-1))


s1 = "AGGTAB"
s2 = "GXTXAYB"
print("LCS:",lcs(s1, s2, len(s1), len(s2)))

