from functools import reduce

creditCardNo=input("Enter a credit card number:")
cList,oList,eList,resList=[],[],[],[]
for i in map(int,creditCardNo):
    cList.append(int(i))
    
for j in range(len(cList)):
    if j%2!=0: 
        oList.append(cList[j])
    else:
        eList.append(cList[j])

print(reduce((lambda x,y:x+y),oList))

for b in range(len(eList)):
    if eList[b]>=5:
        eList[b]=eList[b]*2-10+1
    else:
        eList[b]=eList[b]*2

print(reduce((lambda x,y:x+y),eList))
res=0
resList.extend((oList))
resList.extend((eList))

for i in resList:
    res+=i

if res%10==0:
     print("VALID")
else:
     print("NOT VALID")


#==== RESTART: C:\Users\NYASHTECH-PC\luhn.py ====
#Enter a credit card number:4137894711755904
#43
#37
#VALID

#==== RESTART: C:\Users\NYASHTECH-PC\luhn.py ====
#Enter a credit card number:6499802450273568
#37
#37
#NOT VALID

#==== RESTART: C:\Users\NYASHTECH-PC\luhn.py ====
#Enter a credit card number:8504172191273888
#41
#39
#VALID

#==== RESTART: C:\Users\NYASHTECH-PC\luhn.py ====
#Enter a credit card number:0043668783485480
#31
#41
#NOT VALID 


