def letterCombinations(digits: str):

    ts = {'2': 'abc',
          '3': 'def',
          '4': 'ghi',
          '5': 'jkl',
          '6': 'mno',
          '7': 'pqrs',
          '8': 'tuv',
          '9': 'wxyz'
          }
    res = ['']
    for i in digits:
        bt = []
        for j in ts[i]:
            for k in res:
                bt.append(k + j)
        res = bt
    return res


if __name__ == '__main__':
    while 1:
        try:
            chars = input()
            print(letterCombinations(chars))
        except Exception as e:
            print('输入不规范\t%s' % chars)