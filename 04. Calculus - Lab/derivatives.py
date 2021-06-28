def get_derivative_at_point(function, x, h = 1e-7):
    return (function(x + h) - function(x)) / h

def square(x):
    return x ** 2

def get_left_derivative_at_point(f, x, h = 1e-7):
    return (f(x) - f(x - h)) / h

print(get_derivative_at_point(square, 4))
print(get_left_derivative_at_point(square, 4))

print(get_derivative_at_point(square, 0, 1e-10))