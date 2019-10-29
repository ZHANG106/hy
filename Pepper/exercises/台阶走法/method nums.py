gitclass Solution:
    '''
    新建一个类，将所有的解题的方法封装在里面
    '''
    def method_nums(self, nums: int) -> int:
        '''
        解题的方法
        :param nums: 输入值是总台阶数
        :return: 输出值是走法
        '''
        res = 0
        res1 = 1
        res2 = 2
        if nums == 1:
            res = res1
        elif nums == 2:
            res = res2
        else:
            for i in range(nums-2):
                res = res1 + res2
                res1 = res2
                res2 = res
        return res


if __name__ == '__main__':
    test_ex = input()
    eg = Solution()
    answer = eg.method_nums(test_ex)
    print(answer)
