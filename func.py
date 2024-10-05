# 1) Basic syntax
def func(a, b):
    return a+b

print(func(1,3))
# _________________________________________

# lambda func

sub= lambda a, b: a-b
print(sub(4, 3))
# _________________________________

# pass multipal argument in function one parameter

def sumAll(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sumAll(2,4,6))
# ++++++++++++++++++++++++++++++++++++++++++++++++

