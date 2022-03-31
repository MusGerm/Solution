#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/30 23:30
# @Author : Judy

class Solution(object):
    def __init__(self):
        self.dic = {
            '0':[''],
            '1':[''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def conversion(self, digits):
        '''
        :param digits: str
        :return: List[str]
        '''

        if len(digits) == 1:
            return self.dic[digits]

        words = self.dic[digits[0]]
        result = []

        for i in words:
            for j in self.conversion(digits[1:]):
                result.append(i + j)
        return result

if __name__ == "__main__":
    print(Solution().conversion('40'))