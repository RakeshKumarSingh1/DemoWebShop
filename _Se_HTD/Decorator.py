import time


def outer(func):
    def wrapper(*args, **kwargs):
        print(f"name of the main function is {func.__name__}")
        res= func(*args,**kwargs)
        return abs(res)
    return wrapper

@outer # add=outer(add)
def add(a,b):
    return a+b
print(add(2,4))

@outer

def sub(a,b):
    return a-b
print(sub(6,4))

##Decorator class

class Demo:
    def __int__(self,n):
        self.n=n

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f"name of the main function is {func.__name__}")
            func(*args,**kwargs)
            return wrapper
d=Demo()
@Demo()
def add(a,b):
    print(a+b)
add(2,3)