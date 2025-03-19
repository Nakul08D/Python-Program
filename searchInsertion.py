# Given a sorted array of distinct integer and target value written the index of the target found.If not, return the index whre it would be if it were inserted in order.:

def searchInsert( nums, target):
    left, right = 0, len(nums) - 1
        
    while left <= right:
        mid = left + (right - left) // 2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return left


nums = [1,3,5,6]
target = 7
print(searchInsert(nums,target))


# Find Minmum in Rotated Sorted array:

def find_min(l):
    size=len(l)
    left=0
    right=size-1

    while(left<=right):
        mid=(left+right)//2
        if(l[mid]>l[right]):
            left=mid+1
        else:
            right=mid-1
    return l[left]

l=[3,4,5,1,2]
print(find_min(l))