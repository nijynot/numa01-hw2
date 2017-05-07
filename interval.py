#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:43:04 2017

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt

class Interval:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'I[{}, {}]'.format(self.x, self.y)
    def __add__(self, other):
        if (isinstance(other, Interval)):
            return Interval(self.x + other.x, self.y + other.y)
        else:
            return Interval(self.x + other, self.y + other)
    def __radd__(self, other):
        if (isinstance(other, Interval)):
            return Interval(self.x + other.x, self.y + other.y)
        else:
            return Interval(self.x + other, self.y + other)
    def __sub__(self, other):
        if (isinstance(other, Interval)):
            return Interval(self.x - other.y, self.y - other.x)
        else:
            return Interval(self.x - other, self.y - other)
    def __rsub__(self, other):
        return Interval(other - self.y, other - self.x)
    def __mul__(self, other):
        if (isinstance(other, Interval)):
            xMin = min(self.x * other.x, self.x * other.y, self.y * other.x, self.y * other.y)
            yMax = max(self.x * other.x, self.x * other.y, self.y * other.x, self.y * other.y)
            return Interval(xMin, yMax)
        else:
            return Interval(self.x * other, self.y * other)
    def __rmul__(self, other):
        return Interval(self.x * other, self.y * other)
    def __truediv__(self, other):
        # if (other.x != 0 and other.y != 0):
        try:
            xMin = min(self.x / other.x, self.x / other.y, self.y / other.x, self.y / other.y)
            yMax = max(self.x / other.x, self.x / other.y, self.y / other.x, self.y / other.y)
            return Interval(xMin, yMax)
        # else:
        except ZeroDivisionError:
            return 'ZeroDivisionError: Input interval has a zero as endpoint.'
    def __pow__(self, other):
        if (other % 2 != 0):
            return Interval(self.x ** other, self.y ** other)
        elif (self.x >= 0):
            return Interval(self.x ** other, self.y ** other)
        elif (self.y < 0):
            return Interval(self.y ** other, self.x ** other)
        else:
            return Interval(0, max(self.x ** other, self.y ** other))
    def __contains__(self, other):
        if self.x <= other <= self.y:
            return True
        else:
            return False

def init(start, end, number, diff):
    xl = np.linspace(start, end, number)
    xu = np.linspace(start, end, number) + 0.5
    intervals = []
    for i in range(number):
        intervals.append(Interval(xl[i], xu[i]))
    return intervals

def p(I):
    return 3 * I ** 3 - 2 * I ** 2 - 5 * I - 1

def intervalToPolynomial(intervals):
    polynomials = []
    for i in range(len(intervals)):
        polynomials.append(p(intervals[i]))
    return polynomials

def extractEndpoints(intervals):
    lower = []
    upper = []
    for i in range(len(intervals)):
        lower.append(intervals[i].x)
        upper.append(intervals[i].y)
    return [lower, upper]

# x in this function is the x's of the init.
# Extract the x endpoints of init to get the x axis.
# Extract the endpoints of when passed through the poly function to get y axis.
def plot(x, yl, yu):
    plt.plot(x, yl, x, yu)
    plt.show()