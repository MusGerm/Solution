#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/30 23:30
# @Author : Judy

class Solution(object):
    def __init__(self):
        self.dic = {
            '0':[],
            '1':[],
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
        result = []
        tail = []
        len_d = len(digits)
        if len_d == 0:
            return tail
        elif len_d == 1:
            return self.dic[digits]
        else:
            if '10' in digits or '01' in digits:
                return tail
            elif '1' in digits:
                digits = digits.replace('1', '')
                return self.dic[digits]
            elif '0' in digits:
                digits = digits.replace('0', '')
                return self.dic[digits]

        tail = self.conversion(digits[1:])

        for i in self.dic[digits[0]]:
            for j in tail:
                result.append(i + j)
        return result

if __name__ == "__main__":
    print(Solution().conversion('13'))