#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2022/4/8 16:01 
# @Author : Judy

class Solution(object):
    def transformation(self, s : str,goal : str):
        if s == goal:
            return True
        elif sorted(s) == sorted(goal):
            for i in range(len(s)):
                s2 = s[i:] + s[:i]
                if s2 == goal:
                    return True
        else:
            return False

    def transformation2(self,s : str,goal : str):
        if len(s) == len(goal) and goal in s + s:
            return True
        else:
            return False

if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"
    print(Solution().transformation2(s,goal))


