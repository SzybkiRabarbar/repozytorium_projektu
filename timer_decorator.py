from time import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time()
        v = f(*args, **kwargs)
        print(f"Execution time:{time()-start}")
        if not v == None: return v
    return wrapper

