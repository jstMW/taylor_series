import sympy as sp
import math
def main() -> None:

    #setting up conditions
    x = sp.symbols("x")
    e = math.e
    f = e**x
    n = 5

    constant = compute_constants(f, x, n)
    t = maclaurin(constant, x, n)

    final = sum(t)
    print(final)

def take_derivative(f, x, n):
    return sp.diff(f, x, n)

def take_factorial(number):
    return sp.factorial(number)

def compute_constants(f, x, n):
    constants = []
    for i in range(n+1):
        derivative = take_derivative(f, x, i)
        at_zero = derivative.subs(x, 0)
        factorial = take_factorial(i)
        constants.append(at_zero/factorial)
    return constants


def construct_term(constant, x, n):
    return constant * (x**n)

def maclaurin(constants, x, n):
    terms = []
    for i in range(n+1):
        terms.append(construct_term(constants[i], x, i))
    return terms







if __name__ == '__main__':
    main()