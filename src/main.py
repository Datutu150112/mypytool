from tqdm import tqdm
from .stack import *
from . import stack
def perfect_square_plus_gs(x:int,y:int):
    return f"{x}^{2}+{y}^{2}+{2}*{x}*{y}"
def perfect_square_plus_z(x:int,y:int):
    return (x**2+y**2+2*x*y)
def perfect_square_sub_gs(x:int,y:int):
    return f"{x}^{2}+{y}^{2}-{2}*{x}*{y}"
def perfect_square_sub_z(x:int,y:int):
    return (x**2+y**2-2*x*y)
def glm(x):
    t = base_conversion(x)
    t2 = []
    t2.append(t[0])
    for i in range(len(t)-1):
        t2.append(t[i] ^ t[i+1])
    return t2

def glm2bin(x):
    t = x
    t2 = []
    t2.append(t[0])
    for i in range(len(t)-1):
        t2.append(t2[i]^t[i+1])
    return t2
    
def glm2dex(x):
    t = x
    t2 = []
    t2.append(t[0])
    for i in range(len(t)-1):
        t2.append(t2[i]^t[i+1])
    return base_conversion_dex(t2)

def fast_pow(a,y):
    if(y == 1):
        return a
    if(y==0):
        return 1
    if(y%2 != 0):
        return a * fast_pow(a*a,int(y/2))
    return fast_pow(a*a,int(y/2))

def base_conversion(x,y):
    l = []
    t = x
    while t>0:
        l.append(t%y)
        t//=y
    l.reverse()
    return l

def base_conversion_dex(x):
    t3 = "".join(map(str,x))
    return int(t3,2)
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return [a,b]

def swap1(a,b):
    a += b
    b = a-b
    a = a-b
    return [a,b]

def swap2(a,b):
    t = a
    a = b
    b = t
    return [a,b]

def factorial_recursion(n):
    if(n==0):
        return 1
    return n * factorial_recursion(n-1)
def fibonacci_recursion(n: int):
    if(n<=2):
        return 1
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
def add_int(x: int,y: int):
    return x+y
# def factorial_recursion_tqdm_dy(n,bar,m):
#     bar.update(m)
#     if(n==0):
#         return 1
#     return n * factorial_recursion_tqdm_dy(n-1,bar,m)

# def factorial_recursion_tqdm(n):
#     bar = tqdm(total=1000)
#     if(n==0):
#         num = factorial_recursion_tqdm_dy(n,bar,1000)
#     else:
#         num = factorial_recursion_tqdm_dy(n,bar,1000//n)
#         bar.update(1000-1000//n*n+1)
#     bar.close()
#     return num
# def fibonacci_recursion_tqdm_dy(n,bar,m):
#     bar.update(m)
#     if(n<=2):
#         return 1
#     return fibonacci_recursion_tqdm_dy(n-1,bar,m)+fibonacci_recursion_tqdm_dy(n-2,bar,m)
# def fibonacci_recursion_tqdm(n):
#     bar = tqdm(total=1000)
#     if(n==0):
#         bar.close()
#         return 0
#     else:
#         num = fibonacci_recursion_tqdm_dy(n,bar,1000//n)
#         bar.update(1000-1000//n*n+1)
#     bar.close()
#     return num
def pow(x,y):
    num = 1
    for i in range(y):
        num*=x
    return num

def pow_transform(x,y,n=2):
    return f"{x ** n}^{int(y/n)}"