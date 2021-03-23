# Approximate roots using Newton's Method
import numpy as np
import matplotlib.pyplot as plt
# Create function using x^2 = 1
def f(x):
    y = x ** 2 - 1
    return(y)
# Test function using a logarithmic
def g(x):
    y = np.log(x) - 3
    return(y)
# Function for derivative
def deriv(func, x):
    a = 1e-7
    b = (func(x+a) - func(x-a)) / (2 * a)
    return(b)
# Another Function for testing
def h(x):
    y = 3*x**2 + x
    return(y)
# Function for Netwon Equation
def newton_step(func, x):
    xi = x - (func(x) / deriv(func, x))
    return(xi)
def newton(func, x):
    error = 1
    error_old = 1000000
    roots = []
    new_root = 0
    count = 0
    while abs(error) > 1e-6:
        roots.append(x)
        new_root = newton_step(func, x)
        error = new_root - x
        x = new_root
        if abs(error) > abs(error_old):
            print('The Newton method is diverging.')
            break
        error_old = error
        if count > 50:
            print('Loop has ended because iterations have exceeded 50.')
            break
        count += 1
    return(roots, count)
x = float(input('Please enter a value for x: '))
approx, count = newton(f, x)
print('The list of approximations is: \n',approx)
print('\n The number of iterations was:',count)
# Plotting approximatioins as a funciton of number of iterations
xvals = np.linspace(0, count, len(approx))
plt.plot(xvals, approx, color='b')
plt.xlabel('Number of iterations')
plt.ylabel('Approximation of root')
plt.title('Approximation of root vs. Iteration number')
plt.show()