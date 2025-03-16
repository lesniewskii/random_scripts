class Solution:
    def search(self, nums: int, target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if  nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                 left = mid + 1
            else:
                right = mid - 1

        return -1
    
# Create an instance of Solution
solution = Solution()

nums = [-1,0,3,5,9,12]
target = 9

# Call the search method
res = solution.search(nums, target)

print(res)

        