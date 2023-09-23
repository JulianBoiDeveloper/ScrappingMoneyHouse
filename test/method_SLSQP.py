import numpy as np
from scipy.optimize import minimize

def f(x):
    return x**2 + 1

def con(x):
    return x**3 - x

x0 = [1.0]

res = minimize(f, x0, method='SLSQP', constraints=({'type': 'ineq', 'fun': con}))

print(res.x)