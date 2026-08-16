class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        returnArr = []


        prev = 1
        for i in range(len(nums)):
            prev = prev * nums[i]
            prefix[i] = prev
        
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            prev = prev * nums[i]
            postfix[i] = prev

        for i in range(len(nums)):
            if i == 0:
                returnArr.append(postfix[i + 1])
            elif i == len(nums) - 1:
                returnArr.append(prefix[i - 1])
            else: 
                returnArr.append(prefix[i - 1] * postfix[i + 1])



        return returnArr