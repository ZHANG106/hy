def trap(self, height):
    if len(height) <= 2:
        return 0

    max_height = height[0]
    max_height_index = 0

    # 找到最高点
    for i in range(len(height)):
        h = height[i]
        if h > max_height:
            max_height = h
            max_height_index = i

    area = 0

    # 从左边往最高点遍历
    tmp = height[0]
    for i in range(max_height_index):
        if height[i] > tmp:
            tmp = height[i]
        else:
            area = area + (tmp - height[i])

    # 从右边往最高点遍历
    tmp = height[-1]
    for i in reversed(range(max_height_index + 1, len(height))):
        if height[i] > tmp:
            tmp = height[i]
        else:
            area = area + (tmp - height[i])

    return area
