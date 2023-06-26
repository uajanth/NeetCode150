# Brute Force Solution
# Space Complexity: O(1)
# Time Complexity: O(n^2)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for pos1 in range(len(nums)):
            currentNum = nums[pos1]
            
            for pos2 in range(pos1+1,len(nums)):
                if currentNum == nums[pos2]:
                    return True
                
        return False
    
# Optimal Solution
# Space Complexity: O(n)
# Time Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
                
        return False