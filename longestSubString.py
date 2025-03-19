#Finding the longest substring without repeating characters:

def lss(s):
    
    if(len(set(s)))==len(s):
        return len(s)
    
    substring=""
    maxlen=1

    for i in s:
        if i not in substring:
            substring+=i
            maxlen=max(maxlen , len(substring))
        else:
            substring=substring.split(i)[1]+i

    return maxlen

print("Longest Substring without repeating Character is:",lss("abcdabcdeab"))

#For numbers:

def longest_substring_without_repeating_numbers(nums):
    num_set = set()
    start = 0
    max_length = 0
    max_substr = []

    for end in range(len(nums)):
        while nums[end] in num_set:
            num_set.remove(nums[start])
            start += 1
        num_set.add(nums[end])
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substr = nums[start:end + 1]
    
    return max_substr


nums = [1, 2, 3, 1, 2, 3, 4, 5]
print(longest_substring_without_repeating_numbers(nums))  # Output: [1, 2, 3, 4, 5]

