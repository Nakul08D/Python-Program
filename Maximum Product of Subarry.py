def maxProduct(a):
    if len(a) == 0:
        return 0

    max_so_far = a[0]
    min_so_far = a[0]
    result = max_so_far

    for i in range(1, len(a)):
        curr = a[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max

        result = max(max_so_far, result)

    return result

nums = [2,3,-2,4]
print(maxProduct(nums))