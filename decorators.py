import time

def timeCal(func):
    def wrapper(*args, **keargs):
        start=time.time()
        result= func(*args, **keargs)
        end=time.time()
        print(f"{func.__name__} run in {end-start} time")
        return result
        
    return wrapper

@timeCal
def exfunc(n):
    time.sleep(n)
# ____________________________________________