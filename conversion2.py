#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/31 0:27
# @Author : Judy

class Solution(object):
    def __init__(self):
        self.dic = [
            [""],
            [""],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]

    def conversion2(self, digits,i = 0):
        '''
        :param digits: str
        :param i: default value is 0
        :return:List[str]
        '''
        if i == len(digits) - 1:
            return self.dic[int(digits[i])]

        result = []

        words = self.dic[int(digits[i])]
        for w1 in words:
            for w2 in self.conversion2(digits, i + 1):
                result.append(w1 + w2)
        return result

if __name__ == "__main__":
    print(Solution().conversion2('41'))