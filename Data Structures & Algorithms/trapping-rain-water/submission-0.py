class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r = 0, 1
        # res = 0
        # while r < len(height)-1:
        #     if height[l] <= height[r]:
        #         l = r
        #         r += 1
        #     print(f"l:{l}, r:{r}")
        #     if height[r+1] > height[r]:
        #         r = r+1
        #         area_so_far =  0
        #         for i in range(l, r+1):
        #             if height[i] >= min(height[l], height[r]):
        #                 continue
        #             else:
        #                 area = min(height[l], height[r]) - height[i]
        #                 area_so_far += area
        #         print(area_so_far)
        #     else:
        #         r += 1
        l, r = 0, len(height) - 1
        area_so_far = 0
        index_reached = {}
        while l < r:
            if height[l+1] >= height[l]:
                l += 1
            if height[r-1] >= height[r]:
                r -= 1
            else :
                print(f"l:{l}, r:{r}")
                for i in range(l, r):         
                    if height[i] <= min(height[l], height[r]):
                        area = min(height[l], height[r]) - height[i]
                        print(f"index{i} : area{area}")
                        if i in index_reached.keys():
                            index_reached[i] = max(index_reached[i], area)
                        else:
                            index_reached[i] = area
                    else:
                        continue
                if height[r] >= height[l]:
                    l += 1
                elif height[r] < height[l]:
                    r -= 1
        return sum(index_reached.values())





            

            
        