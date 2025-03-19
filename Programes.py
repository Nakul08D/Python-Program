#Python Programes:

#Python Program for sorting elements of an Array by Frequency

def sort_by_frequency(arr):
    frequency={}
    for i in arr:
        if i not in frequency:
            frequency[i]=1
        else:
            frequency[i]+=1
    
    sorted_element=sorted(arr,key=lambda x:(-frequency[x],x))
    return sorted_element


arr = [4, 5, 6, 5, 4, 3]
sorted_arr = sort_by_frequency(arr)
print(sorted_arr)  # Output: [4, 4, 5, 5, 3, 6]

#Minimum no. of merge operations required to make an array palindrome in Python

def find(array):
    ans=0
    i=0
    j=len(array)-1
    while(i<j):
        if(array[i]==array[j]):
            i+=1
            j-=1
        elif(array[i]>array[j]):
            j-=1
            array[j]+=array[j+1]
            ans+=1
        else:
            i+=1
            array[i]+=array[i-1]
            ans+=1
            
    return ans


array = [2, 10, 12, 26, 3, 22, 2]
print("Total number of merging operation required is", find(array))

#Python Program to Find Longest Consecutive Subsequence

def LongestConseqSubseq(arr, l):
    val = []
    c = 0
    print(arr)
    for i in range(l):
        n = 1
        while arr[i] + n in arr:
            c += 1
            n += 1
        val.append(c + 1)
        c = 0
    print(val)
    return max(val)


array = [7, 8, 1, 5, 4, 3] #[1,  3,4,5  ,7,8]
                           # 1      3     2
print("Longest Consecutive Subsequence :", LongestConseqSubseq(array, len(array)))