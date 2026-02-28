

from operator import add


def add_print(a, b):
    print(add(a, b))
          
add_print(a=5, b=10)

def add_return(a, b):
    return a + b

result = add_return(a=5, b=10)

