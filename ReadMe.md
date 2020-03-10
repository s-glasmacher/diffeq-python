# Sympy Documentation

Sympy can be found here: https://www.sympy.org/en/index.html

It is a free Python library for symbolic mathematics. 

## Installation

Install through `pip install sympy`

## Why Sympy?
We wanted to use symbolic mathematics to find the intersection of a constant function and the solution of a differential equation. 

Because traditional solvers only evaluate the solution *y* on a given array of t-values, finding the point where *y* reaches a given constant would have involved a lot of trial and error. 

Symbolic mathematics allows us to solve a differential equation and receive the solution *y* as a response. Then we can use it to solve the equation of *y*=constant and receive the points of intersection as response. 

## Technical details for Sarah to remember

- Symbol('t') creates a symbol to be used as a Function Parameter which can later be substituted for numerical values
- Function('y')(x) creates a Function. A Function can also be created as "Function('y') - however this way breaks the Equation expressing the differential equation by making it always be **False**. Then we can not solve it to find out *y*. 
	- in the result of this we can insert numerical values the following way: f.subs(x, 0.7) where f is a Function and x the Symbol provided as its parameter
- Derivative(f, x) creates a Function representing the derivative of the Function f with respect to the variable x
- Equation(left_side, right_side) to express an equation. Example: Equation(f_strich, what_we_know_about_fstrich) for differential equations
- dsolve(eq) to solve an Equation eq that represents a differential equation. 
	- provide the parameter ics={f(x0): y0} for initial values
	- calculate f(x0) through f.subs(x, x0) as described above. f(x0) does not work because f is not callable the way we created it above.
- solve(eq) for regular intersection solving
- parse_expr(string, evaluate=False) to transform a string into a Sympy Expression. Example: "exp(t)*y(t)"
	- from sympy.parsing.sympy_parser import parse_expr
	
# PyZMQ

### Installation
Best install through pip: 
"pip install pyzmq"
If not already available, install zeromq before: "sudo apt-get install libzmq3-dev" (Debian-based, tested on Ubuntu)

## Available documentation
Sadly lacking. I know, this is a theme here. 

https://zeromq.org/get-started/?language=python&library=pyzmq# Here the Pyzmq examples are missing. At some point I want to see if maybe I can contribute them. 

https://pyzmq.readthedocs.io/en/latest/api/index.html This describes the basic classes. However it is lacking in examples and "How-To"s. 

## Technical details

- first create a context by: ctx = zmq.Context.instance()
- in this we can create a socket: socket = ctx.socket(zmq.REP) with a ZMQ-Type such as Reply in this case
- receive a message: socket.recv(). 
	- note that, if the message has multiple parts, this will only receive part of the message and has to be called again for every part. This is unlike the functionality in C. 
	- the message is furthermore received as Bytes, and so has to be decoded to get the string back. (msg.decode())
	
- socket.send(msg) to send a message. Again, this needs to be in Bytes, so encode a string first by calling string.encode() on it
	