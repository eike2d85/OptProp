from scipy.optimize import differential_evolution
import numpy as np
import Blade_Element_Main as BEM
    

bounds = [(-5, 5), (-5, 5)]
result = differential_evolution(BEM.Blade_Element_Main, bounds)
# result.x, result.fun
print(result)