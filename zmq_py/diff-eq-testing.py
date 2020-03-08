from sympy import Function, Symbol, Eq, exp, Derivative, dsolve, solveset
from sympy.parsing.sympy_parser import parse_expr
#from sympy.functions.elementary.exponential import exp


#create an undefined function 
t = Symbol('t')
#oder f = Function('f')(x)

# build the derivative of a function with f(x).diff(x)
# or directly with Derivative(f, x)
# both give you the same thing for an undefined function


y = Function('y')(t)
y_strich = Derivative(y, t)
print('ystrich', y_strich)

# Eq forms an Equality
eq = Eq(y_strich, parse_expr('exp(t)*y(t)', evaluate=False))
print(eq)
# dsolve without starting value gives us solution involving C1 eg
print(dsolve(eq, ics={y.subs(t, 0): 1}))

# converts string to sympy expression
# print(parse_expr('exp(t)*y(t)', evaluate=False))




