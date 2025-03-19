# String Permutation:

result=[]

def permute(st,i,size):
    if(i==size):
        result.append(''.join(st))
    else:
        for j in range(i,size):
            st[i],st[j]=st[j],st[i]
            permute(st,i+1,size)
            st[i],st[j]=st[j],st[i]

a="yup"
permute(list(a),0,len(a))

print("Result is:",result)

#2nd Way:
# def permute(st,i=0):
 
#     if(i==len(st)):
#         print(''.join(st))
#     for j in range(i,len(st)):
#         word=[w for w in st]
#         word[i],word[j]=word[j],word[i]
#         permute(word,i+1)
        


# a='yup'
# permute(a)

#for list:
result=[]
def permute(s, i, l):
    if(i==l):
       result.append(s.copy())

    else:
        for j in range(i,l):
            s[i],s[j] = s[j], s[i]
            permute(s, i+1, l)
            s[i],s[j] = s[j], s[i]


a=[1,2,3]
permute(a, 0, len(a))
print((result))

# Using s.copy() in the line result.append(s.copy()) is essential because lists in Python are mutable. When you modify a list in place, those changes are reflected everywhere that list is referenced. Without using s.copy(), all elements in the result list would end up referencing the same list object s, which gets modified throughout the recursive permutations.