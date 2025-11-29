def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        S:
            - given: int array height
            - return: max amount of water container can store
        P:
            - need opposite end pointers
                - first calc max water of ends (width * height)
                    - w = l-r indices
                    - h = min (height[l], height[r])
        I:
            - max variable
            - while loop with l and r pointers
                - calc water
                - replace max
                -iterate lower height
        C:
        D:

        """
        max_w = 0
        l = 0
        r = len(height)-1
        while l < r:
            w = r-l
            h = min(height[l], height[r])
            water = w * h
            max_w = max(max_w, water)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return max_w
print(maxArea([1,8,6,2,5,4,8,3,7]))