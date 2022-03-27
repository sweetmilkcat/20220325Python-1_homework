# -*- coding: utf-8 -*-
"""
data=[99,1,10,6,88,60] (請使用迴圈的方式撰寫)
請將data 排序 由小到大 並 印出排序後結果[1,6,10,60,88,99]
或由大到小
"""
data=[99,1,10,6,88,60]
number=[]
while len(data):
    Min=data[0]
    minKey=0
    for i in range(0,len(data)):
        if  data[i] <Min:
            Min=data[i]
            minKey=i 
    number.append(data.pop(minKey))
print(number)

"""
sort & reverse
"""
data=[99,1,10,6,88,60]
number=sorted(data,reverse=False)
print(number)