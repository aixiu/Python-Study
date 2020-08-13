#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('现原形吧你。')
    elif len(args) == 2:
        print('Hello {}'.format(args[1]))
    else:
        print('太多了，我不想数了')

if __name__ == '__main__':
    test()
