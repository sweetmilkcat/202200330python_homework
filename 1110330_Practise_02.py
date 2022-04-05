# -*- coding: utf-8 -*-
"""
有4個數字1,2,3,4
可組成幾個互不相同的三位數字
"""
count=0
for i in range(1,5):
    for j in range(1,5):
        for x in range(1,5):
            if (i !=j and j!=x and i!=x):
                count+=1
                print(i,j,x,sep="")
print("1,2,3,4總共可組成{}個三位數字".format(count))

