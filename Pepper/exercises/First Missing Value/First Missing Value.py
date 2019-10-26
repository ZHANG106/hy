from typing import List

def firstMissingPositive(nums:List[int])->int:
	result = (i for i in range(sorted(nums)[-1]) if i not in nums)
	return next(result)



