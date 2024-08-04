# Problem :- https://leetcode.com/problems/subarray-sum-equals-k/description/

#  Solution :- https://www.youtube.com/watch?v=frf7qxiN2qU

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_map = {0: 1}
        print(sum_map)
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sum_map:
                count += sum_map[current_sum - k]
            sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
        
        return count
