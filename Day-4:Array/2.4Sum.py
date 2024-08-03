#  Problem :- https://leetcode.com/problems/4sum/description/

# Solution :- https://www.youtube.com/watch?v=eD95WRfh81c&ab_channel=takeUforward

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums) # size of the array
        st = set()

        # checking all possible quadruplets:
        for i in range(n):
            for j in range(i+1, n):
                hashset = set()
                for k in range(j+1, n):
                    # taking bigger data type to avoid integer overflow:
                    sum_ = nums[i] + nums[j] + nums[k]
                    fourth = target - sum_
                    if fourth in hashset:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    # put the kth element into the hashset:
                    hashset.add(nums[k])

        ans = [list(t) for t in st]
        return ans
