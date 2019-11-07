def trap(height) -> int:
    result = 0
    for i in range(max(height), 0, -1):
        count_i = height.count(i)
        index_i = [i for i, x in enumerate(height) if x == max(height)]
        if count_i > 1:
            for j in range(len(index_i)-1):
                result += i*(index_i[j+1]-index_i[j]-1)-sum(height[index_i[j]+1:index_i[j+1]])
                height[index_i[j]] = i-1
                height[index_i[j+1]] = i-1
            remove = sorted([i for i in range(index_i[0]+1, index_i[-1]) if i not in index_i], reverse=True)
            for k in range(len(remove)-1, 0, -1):
                del height[remove[k]-1:remove[k-1]+1]
        elif count_i == 1:
            height[index_i[0]] = i-1
    return result



