import zmq
from sympy import Function, Symbol, Eq, Derivative, dsolve, solve
from sympy.parsing.sympy_parser import parse_expr

ctx = zmq.Context.instance()
reply_socket = ctx.socket(zmq.REP)
reply_socket.bind("tcp://*:5555")

msg = reply_socket.recv()
# decode to go from bytes-object back to a string
function_string = msg.decode()

msg = reply_socket.recv()
function_name = msg.decode()

msg = reply_socket.recv()
function_variable = msg.decode()

msg = reply_socket.recv()
initial_x_string = msg.decode()
initial_x = float(initial_x_string)

msg = reply_socket.recv()
initial_f_string = msg.decode()
initial_f = float(initial_f_string)

msg = reply_socket.recv()
constant_string = msg.decode()
constant = float(constant_string)


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

if len(intersection) > 0:
    reply_message = str(intersection[0]).encode()
    reply_socket.send(reply_message)