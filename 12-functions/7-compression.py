# encoding: utf-8
l1 = [1, 2, 3, -1, 4]
l2 = [num for num in l1 if num > 0]
print l1
print l2

s = ["H", "e", "l", "l", "o"]
l2 = [c * num for c in s
        for num in l1
            if num >  0]
print l1
print l2
