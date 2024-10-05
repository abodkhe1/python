# 1) child= 1 to 13, teenager= 13 to 19, Adult= 20 to 59, senior = 60+

# age=input('Enter your age = ')
# intage=int(age)
intage=20

if intage < 13:
    print('user is child')
elif intage>=13 | intage<20:
    print('user is teenager')
    
elif intage>=20 | intage<=59:
    print('user is Adult')
else:
    print('user is a senior')
# ________________________________________

# 2)childern movie ticket=200 , adult movie ticket = 400
# wednesday all ages 5% discount
# age less than 18 = children, 18 above = adult

age=34
day='monday'
price=200 if age < 18 else 400
discount =5

if day == 'wednesday':
    ticketAmt=price*discount/100
    ticketAmt=price-ticketAmt
    # print('ticket amount= ', ticketAmt)
        
else:
   print('ticket amount=',price)
# _________________________________

# 3) assign grade based on student score
# A=90-100 
# B=80-89 
# C=70-79 
# D=60-69 
# F=less than 60 

score=91
if score >=90 and score <= 100:
    print('Grade = A')
elif score >=80 and score <= 89:
    print('Grade = B')
elif score >=70 and score <= 79:
    print('Grade = C')
elif score >=60 and score <= 69:
    print('Grade = D')
elif score < 60:
    print('Grade = F')
else:
    print('ENter SCore less than and equal 100')