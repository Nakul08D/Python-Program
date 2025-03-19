#Arrange given numbers to form the biggest number :

def largestNumber(a):
    if(len(a)==0):
        return 0
    for i in range(len(a)):
        a[i]=str(a[i])

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]+a[j]<a[j]+a[i]):
                a[i],a[j]=a[j],a[i]
    
    result=''.join(a)
    return result


a = [54, 546, 548, 60]
print(largestNumber(a))
    