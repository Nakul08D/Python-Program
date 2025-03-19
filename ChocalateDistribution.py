#Chocalate Distribut Problen

'''Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.'''

def findMinDiff(l, n, m):
    if(n==0 or m==0):
        return 0
    
    # Number of students cannot be more than
    # number of packets
    if(n<m):
        return -1
    
    l.sort()

    min_diff=l[n-1]-l[0]

    for i in range(len(l) - m + 1):
        min_diff = min(min_diff,  l[i + m - 1] - l[i])

    return min_diff

l = [7, 3, 2, 4, 9, 12, 56]
m = 3  # Number of students
n = len(l)
print("Minimum difference is", findMinDiff(l, n, m))