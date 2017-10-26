# decorator


def log_params(func):
    def log_params_inner(*args, **kwargs):
        #preprocessing
        #call the function with params
        #postprocessing and return result
        print args, kwargs
        print "{} called with params: {}".format(str(func), str(args))
        ret = func(*args, **kwargs)
        print "{} was called successfully. Result: {}".format(str(func), ret)
        return ret

    return log_params_inner


@log_params
def addn(a,b,c):
    return a+b+c

@log_params
def sub(a,b):
    return a-b

@log_params
def mul(a,b,c,d):
    return a*b


print addn(4, 5, 3)
print sub(5, 6)
print mul(5, 6, 4, d=3)
