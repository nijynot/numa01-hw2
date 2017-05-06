#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:43:04 2017

@author: tony
"""

class Interval:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __repr__(self):
        return '[{}, {}]'.format(self.x, self.y)
    def __add__(self, other):
        return Interval(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Interval(self.x - other.y, self.y - other.x)
    def __mul__(self, other):
        xMin = min(self.x * other.x, self.x * other.y, self.y * other.x, self.y * other.y)
        yMax = max(self.x * other.x, self.x * other.y, self.y * other.x, self.y * other.y)
        return Interval(xMin, yMax)
    def __truediv__(self, other):
        # if (other.x != 0 and other.y != 0):
        try:
            xMin = min(self.x / other.x, self.x / other.y, self.y / other.x, self.y / other.y)
            yMax = max(self.x / other.x, self.x / other.y, self.y / other.x, self.y / other.y)
            return Interval(xMin, yMax)
        # else:
        except ZeroDivisionError:
            return 'ZeroDivisionError: Input interval has a zero as endpoint.'
    def __contains__(self, other):
        if self.x <= other <= self.y:
            return True
        else:
            return False