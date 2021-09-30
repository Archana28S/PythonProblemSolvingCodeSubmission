# Problem Set 2
# Name: Archana Sharma
# Time Spent: 1day




##Problem 1:Implement the evaluate_poly function. This function evaluates a polynomial function for the given x value. It takes in a tuple of numbers poly and a number x. By number, we mean that x and each element of poly is a float. evaluate_poly takes the polynomial represented by poly and computes its value at x. It returns this value as a float.

def evaluate_poly(poly, x):
    total=0
    for i in poly:
        total+= (poly[poly.index(i)])*(x**(poly.index(i)))
    return total
    eqn=tuple(poly)
    result=eqn[0]
    for i in range(1,len(eqn)):
        total+= eqn[i](x*1)
        print(eqn[i],total)
        print(float(total))
        print(evaluate_poly(poly,-13))
poly=(0.0, 0.0, 5.0, 9.3, 7.0)
x=-13
print(evaluate_poly(poly, x))

##Test Pass

##Problem 2:Implement the compute_deriv function. This function computes the derivative of a polynomial function. It takes in a tuple of numbers poly and returns the derivative, which is also a polynomial represented by a tuple. 

def compute_deriv(poly):
    total=()
    for i in range(1,len(poly)):
        total += (poly[i]*(i),)
    return total

poly =(-13.39,0.0,17.5,3.0,1.0)
print(compute_deriv(poly))

##Test Pass


##Problem 3:Implement the compute_root function. This function applies Newton’s method of successive approximation as described above to find a root of the polynomial function. It takes in a tuple of numbers poly, an initial guess x_0, and an error-bound epsilon. It returns a tuple. The first element is the root of the polynomial represented by poly; the second element is the number of iterations it took to get to that root. 
##The function starts at x_0. It then applies Newton’s method. It ends when it finds a root x such that the absolute value of f(x) is less than epsilon, i.e. f(x) is close enough to zero. It returns the root it found as a float.

def compute_root(poly,x_0,epsilon):
    in_c = 1
    while (abs(evaluate_poly(poly,x_0)) > epsilon):
        in_c += 1
        x_0 = x_0 - (evaluate_poly(poly,x_0)/(evaluate_poly(compute_deriv(poly),x_0)))
        return(x_0,in_c)

poly= (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = 0.0001
print(compute_root(poly,x_0,epsilon))

##My answer is not correct for 3rd problem.I tried to solve the problem but do not know how it can be corrected##




