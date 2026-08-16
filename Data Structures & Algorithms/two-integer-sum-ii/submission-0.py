class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointers

        # 1 2 3 4 
        # 1 1 1
        # 1 2 3
        # 5 4 3 4

        # 1 2 3 4 8
        # 1 1
        # 1 2
        # 6 5

        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:

            high_diff = target - numbers[l]
            low_diff = target - numbers[r]

            if high_diff > numbers[r] or low_diff > numbers[l]:
                l += 1
            elif low_diff < numbers[l] or high_diff < numbers[r]:
                r -= 1

        return [l + 1, r + 1]