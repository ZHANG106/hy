dic = {2: ['a', 'b', 'c'],
       3: ['d', 'e', 'f'],
       4: ['g', 'h', 'i'],
       5: ['j', 'k', 'l'],
       6: ['m', 'n', 'o'],
       7: ['p', 'q', 'r', 's'],
       8: ['t', 'u', 'v'],
       9: ['w', 'x', 'y', 'z']}
number = input()
med1 = dic[int(number[0])]
result = []
for i in range(len(number)-1):
    med2 = dic[int(number[i+1])]
    for letter in med2:
        result += list(map(lambda x: x+letter, med1))
    med1 = result
print(result)