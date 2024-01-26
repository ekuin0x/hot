import sympy as sym
import numpy as np


x=sym.Symbol('x')

f=x**2+10*x+21

diff_f=sym.diff(f,x)
diff_f

f_func=sym.lambdify(x,f,'numpy')
diff_f_func=sym.lambdify(x,diff_f,'numpy')

def newtonMethod(x0,iterationNumber, f,df):
    x=x0
    
    for i in range(iterationNumber):
        
        x=x-f(x)/df(x)
    
    residual=np.abs(f(x))
    return x,residual

solution,residual = newtonMethod(-2,200,f_func,diff_f_func)

print(solution)