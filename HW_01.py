# -*- coding: utf-8 -*-
"""
1.由系統自動產生6個不重複的數字(1~100)
2.由使用者自行輸入6個號碼
3.先印出系統產生的6個號碼
4.再印出使用者中了幾個，中兩個獲得10顆蘋果，中3個獲得20顆蘋果，中4個獲得30顆蘋果，中5個獲得40顆蘋果，中6個獲得50顆蘋果
"""
import random
prizE=[0,0,10,20,30,40,50]
numbers=list()
while True:
    num=random.randint(1,100)
    if numbers.count(num)==0:
        numbers.append(num)
    if len(numbers)== 6:
        break
print (numbers)
keynumber=[]
while len(keynumber)<6:
    num=int(input("請輸入數字(1~100)不重複:"))
    if keynumber.count(num)==0:
        keynumber.append(num)
    else:
        print("數值重複請重新輸入!")
count=0
for a in numbers:
    for b in keynumber:
        if a == b:
            count+=1
if count <2:            
    print("可惜!沒得獎~下次再加油!")
else:
    print("中了{}個號碼!恭喜獲得{}個蘋果~".format(count,prizE[count]))

