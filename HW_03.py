# -*- coding: utf-8 -*-
"""
練習題
請印出:
999999999
 8888888
  77777
   666
    5
   666
  77777
 8888888
999999999
"""
count=9
num=9
for i in range(9,4,-1):
    print(" "*(num-i),sep="",end="")
    for j in range(count):
        print(i,sep="",end="")       
    count-=2
    print()
count=3
for i in range(6,10):
    print(" "*(num-i),sep="",end="")
    for j in range(count):
        print(i,sep="",end="")       
    count+=2
    print()