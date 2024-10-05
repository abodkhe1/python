# 1) fruits ripeness checker based on fruits color
# fruit= banana
# green=Unripe
# yellow=Ripe
# brown=Overripe
fruit= 'Banana'
color='green'

if fruit =='Banana':
    if color=='green':
        print('Unripe')
    elif color=='yellow':
        print('Ripe')
    elif color=='brown':
        print('Overripe')
    else:
        print('please select proper fruit color')
else:
    print('please choose elegible fruits')
# _____________________________________________________

# 2) weather actively suggetion
# based on weather
# sunny=go fo walk
# rainy = read a book
# snowy=build a snowman
weather='sun1ny'

output='go fo walk' if weather=='sunny' else 'read a book' if weather=='rainy' else 'build a snowman' if weather=='snowy' else 'Enter actively weather'

# print(output)

# 3) transporation mode select based on distans
# less than 3 km = walk
# 3 to 15 km =bike
# grater than 15 km = car

distance = 16

if distance < 3:
    print('transportatin on walking distance')
elif distance >=3 and distance <=15:
    print('transport on Bike')
else:
    print('transportatin on car')
    
# __________________________________________________

# 4) cofee customization
# available cofee in small, medium, large
# also available extra shot

cofee_order='small'
extra_shot=False

if extra_shot:
    print(cofee_order,'cofee with extra shot')
else:
    print(cofee_order,'cofee')
    
# ____________________________________________

# 5)password strength checker

# less than 6 char = Weak
# 6 to 10 char = Medium
# grater than 10 char = Strong
    
password='AJIT'

if len(password) < 6:
    print('passwoed strength weak') 
elif len(password) >=6 and len(password) <=10:
    print('passwoed strength medium')
else:
    print('passwoed strength strong')
# ______________________________________________

# 6) Leap year checker
# leap year divisible by 4 but not by 100 unless also divisible 400

# year=2024 # leap year
# year=1900 # not leap year
year=2000 # leap year

if year%4==0:
    if year%100==0:
        if year%400==0:
            print('its Leap year')
        else:
            print('its not leap year')
    else:
        print('its Leap Year')
else:
    print('its not leap year')
# ____________________________________________

# 7)food recomandation age wise
# dog leass than 2 years =puppy food
# cat grater than 5 year =senior cat food

animal='Dog'
age=2
food=''

if animal=='Cat':
    food= 'junior '+animal+' food' if age <=5 else 'sinior '+animal+' food'
elif animal=='Dog':
    food= 'puppy food' if age < 2 else 'sinior '+animal+' food'


print('recomanded '+food)
    

