# 3Sum:
def threeSum(l):
    target=0
    l.sort()
    s=set()
    n=len(l)
    for i in range(n):
        j=i+1
        k=n-1
        while(j<k):
            sum=l[i]+l[j]+l[k]
            if(sum == target):
                s.add((l[i], l[j], l[k]))
            if(sum < target): 
                j+=1
            else:
                k-=1
    
    return list(s)

l=[-1,0,1,2,-1,-4]
print(threeSum(l))
