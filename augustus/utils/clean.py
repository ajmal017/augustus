import arrow

def make_it_float(func):
    @wraps(func)
    def wrapper(*args,**kargs):
        return float(func(*args,**kargs))
    return wrapper