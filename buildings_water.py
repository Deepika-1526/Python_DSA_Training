def trap_water(heights):
    if len(heights) == 0:
        return 
    
    left = 0
    right = len(heights) - 1
    left_max = heights[left]
    right_max = heights[right]
    water_trapped = 0
    
    while left < right:
        if heights[left] < heights[right]:
            left += 1
            left_max = max(left_max, heights[left])
            water_trapped += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water_trapped += right_max - heights[right]
    
    return water_trapped

#heights = [2, 5, 2, 3, 6, 7, 1, 0, 5]
#heights = [4,3,4,5,6,1,0,6,7
#heights = [2,4,2,3,4,4,1,0,4,4]
heights=[9,4,5,6,2,4]
water_units = trap_water(heights)
print(water_units)
