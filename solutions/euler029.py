#!/usr/bin/env python
"""
Solution to Project Euler Problem 29
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/


Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    22=4, 23=8, 24=16, 25=32
    32=9, 33=27, 34=81, 35=243
    42=16, 43=64, 44=256, 45=1024
    52=25, 53=125, 54=625, 55=3125

If they are then placed in numerical order, with any repeats removed, we get
the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100
and 2 ≤ b ≤ 100?
"""


def power_combinations(m):
    return {a ** b for a in range(2, m + 1) for b in range(2, m + 1)}


def test():
    assert 15 == len(power_combinations(5))


def run():
    print(len(power_combinations(100)))


if __name__ == '__main__':
    test()
    run()
