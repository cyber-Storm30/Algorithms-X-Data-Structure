"""
Given an int array which might contain duplicates, find the largest subset
of it which form a sequence.

Example:
    Input  -> [1, 6, 10, 4, 7, 9, 5]
    Output -> [4, 5, 6, 7]

Expected:
    Time Complexity: O(n)
"""
from copy import copy


arr = [1, 6, 10, 4, 7, 9, 5]

arr = set(arr)  # Time Complexity : O(n)
upr_limit = max(arr)  # Time Complexity : O(n)
lwr_limit = min(arr)  # Time Complexity : O(n)

count = 0
final_count = 0

result = []
tmp_arr = []

for i in range(lwr_limit, upr_limit+1):  # Time Complexity : O(n)
    if i in arr:
        count += 1
        tmp_arr.append(i)
    else:
        if final_count < count:
            final_count = count
            result = copy(tmp_arr)

        count = 0
        tmp_arr = []

print(result)
