from sympy import Function, Symbol, Eq, Derivative, dsolve, solveset, solve
from sympy.parsing.sympy_parser import parse_expr

# Task: find meeting point between a value (constant function) and a function y
# the function y has to first be found as a solution of a differential equation

# inputs: function definition (string), variables (string - if needed), constant value (string bc of zmq if possible)
function_string = "exp(t)*y(t)"
function_name = "y"
function_variable = "t"
initial_x = 0.0
initial_f = 1.0
# can be multiple and we could split on comma etc
other_symbols = "a"
constant = 1.0

x = Symbol(function_variable)
f = Function(function_name)(x)
f_strich = Derivative(f, x)

function_definition = parse_expr(function_string, evaluate=False)
print('f def:', function_definition)
eq = Eq(f_strich, function_definition)
print('eq:', eq)
solution = dsolve(eq, ics={f.subs(x, initial_x): initial_f})
print('solution:', solution)

second_eq = Eq(solution.rhs, constant)
intersection = solve(second_eq)

print('intersection:', intersection)