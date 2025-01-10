class FindDuplicate:
    def findDuplicate(self, nums: List[int]) -> int:
        singles = set()
        for n in nums:
            if n in singles:
                return n
            else:
                singles.add(n)