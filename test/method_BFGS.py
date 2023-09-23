import numpy as np
from scipy.optimize import minimize
from multiprocessing import Pool

def optimize_function(x):
    # Définir votre fonction d'optimisation ici
    return x**2 + 2*x + 1

def parallel_optimization(optimize_function, x0):
    with Pool(processes=12) as pool:
        result = minimize(optimize_function, x0, method='BFGS', options={'disp': True})
        return result.x

if __name__ == '__main__':
    x0 = np.array([0.0])
    optimized_x = parallel_optimization(optimize_function, x0)
    print(optimized_x)