<<<<<<< HEAD
dic = {2: ['a', 'b', 'c'],
       3: ['d', 'e', 'f'],
       4: ['g', 'h', 'i'],
       5: ['j', 'k', 'l'],
       6: ['m', 'n', 'o'],
       7: ['p', 'q', 'r', 's'],
       8: ['t', 'u', 'v'],
       9: ['w', 'x', 'y', 'z']}
number = list(set(input()))
med1 = dic[int(number[0])]
result = []
for i in range(len(number)-1):
    med2 = dic[int(number[i+1])]
    for letter in med2:
        result += list(map(lambda x: x+letter, med1))
    med1 = result
print(result)
=======
from typing import List


class Solution:
    def letterCombinations(self, digits:str)-> List[str]:
        pass
>>>>>>> f783d39a902a2ad088f55676a7fa6e3a9eea20f1
