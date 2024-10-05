# 1) count positive number in list

numList=[1,3,5,-2,-5,2,-6,6,7,-3]
sum=0
for num in numList:
    if(num > 0):
        sum+=1

# print(sum)

# ---------------------------------------

# 2) 0 to n number all even number sum

n =10
evenSum=0
for i in range(n+1):
    if i % 2 == 0:
        evenSum+=i

# print('sum of 1 to',n,'number =', evenSum)

# ____________________________________________

# 3) create table but skip fifth ittration

number=3
for i in range(1, 11): 
    if i!=5:
        print(number,'x',i,'=',number*i)
# ______________________________________________

# 4) reverse string using loops

string='AJIT'
rev=''

for char in string:
    rev=char+rev
print(rev)  
# ________________________

# 5) find first non repeated character in string

newString='anyusna'

for char in newString:
    count=newString.count(char)
    if count==1:
        print('first non repeated character=',char)
        break
# ______________________________________________________

# 6) calculate factorial in number using while loop

fnumber=5
fact=1

while fnumber > 0:
    fact*=fnumber
    fnumber-=1
# print(fact)


# ---------------------------------------------------

# 7) ask user get number check this number between 1 to to

# while True:
#     val=int(input('Enter number\n'))
#     if(val > 0 and val <= 10 ):
#         print('True')
#     else:
#         print('False')
        
# _______________________________________________________

# 8) chek number is prime or not

chknum=29
isPrime=True
if chknum > 1:
    for i in range(2, chknum):
        if chknum % i==0:
            isPrime=False
            break
else:
    isPrime = False
        
# print(isPrime)
            
# _______________________________________________

# 9) find duplicate element in array print this

duplicateList=['apple', 'mango', 'apple', 'watermelon', 'graps']

for dup in duplicateList:
    count=duplicateList.count(dup)
    if count > 1:
        print(dup, 'is a duplicate element count=', count)
        break

# _________________________________________

import time, datetime

waitTime=1
maxRet=5
attempt=0
# current_datetime = datetime.datetime.now()
# print(current_datetime) 
# exit()
while attempt < maxRet:
    print('Attempt', attempt+1,'-wait time', waitTime)
    time.sleep(waitTime)
    waitTime*=2
    attempt+=1
 # ___________________________________________________


# behind in loops

