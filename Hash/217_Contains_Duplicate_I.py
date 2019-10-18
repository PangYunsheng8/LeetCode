class Solution:
    def containsDuplicate(self, nums) -> bool:
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                return True
        return False