from sympy import *

def cleanfunction(function):
    func = function
    # funclen = [i for i in range(len(func))]
    funclen = len(func)
    i = 0
    while i < funclen:

        # get the expression inside sqrt()
        # and skip adding '*'
        if (i + len('sqrt(')) < funclen:
            if func[i:i + len('sqrt(')] == 'sqrt(':
                i = i + len('sqrt(')
                continue

        # get the expression inside Abs()
        # and skip adding '*'
        if (i + len('Abs(')) < funclen:
            if func[i:i + len('Abs(')] == 'Abs(':
                i = i + len('Abs(')
                continue

        # insert '*' for multiplication
        # if a number is beside a variable
        if (func[i]).isnumeric():
            if i == len(func) - 1:
                break
            if (func[i + 1].isalpha()):
                func = func[:i + 1] + '*' + func[i + 1:]

        # insert '*' for multiplication
        # if a variable is beside another variable
        if (func[i]).isalpha():
            if i == len(func) - 1:
                break
            if (func[i + 1].isalpha()):
                func = func[:i + 1] + '*' + func[i + 1:]
            if (func[i + 1].isnumeric()):
                func = func[:i + 1] + '*' + func[i + 1:]


        symbols = ['*', '^', '/', '(', ')', ' ']

        # insert '*' for multiplication
        # if a variable or number is beside a '('
        if func[i] == "(":
            if i == 0:
                i += 1
                continue
            elif func[i - 1] not in symbols:
                func = func[:i] + '*' + func[i:]
            elif func[i - 1] == ')':
                func = func[:i] + '*' + func[i:]

        # insert '*' for multiplication
        # if a variable or number is beside a ')'
        if func[i] == ")":
            if i == len(func) - 1:
                break
            if func[i + 1] not in symbols:
                func = func[:i + 1] + '*' + func[i + 1:]
        
        funclen = len(func)
        i += 1

    return func

def evaluate(function, variables):
    answer = Function('')(cleanfunction(function))

    # substitute the values of the variables to the function
    for v in variables.keys():
        # v = variable, variables[v] = value of variable
        answer = answer.subs(v, cleanfunction(variables[v]))
    # answer = answer[1:len(str(answer))]
    answer = str(answer)
    # remove the parenthesis
    answer = answer[1:len(answer) - 1]

    # replace for muggle readability
    answer = answer.replace("**", "^")
    answer = answer.replace("*", "")
    return answer


def operate(function1, function2, x, operation):
    f1 = str(Function('')(cleanfunction(function1)))
    f2 = str(Function('')(cleanfunction(function2)))
    expression = f1 + operation + f2
    answer = simplify(expression)
    answer = str(cancel(answer))
    answer = evaluate(answer, {'x': x})
    # answer = str(answer.subs(answer, x))
    # answer = answer[1:len(answer) - 1]
    # answer = answer.replace("**", "^")
    # answer = answer.replace("*", "")
    return answer


def composite(function1, function2, x):
    f1 = str(Function('')(cleanfunction(function1)))
    f2 = str(Function('')(cleanfunction(function2)))
    answer = evaluate(f1, {'x': f2})
    answer = evaluate(answer, {'x': x})
    answer = str(simplify(cleanfunction(answer)))
    answer = answer.replace("**", "^")
    answer = answer.replace("*", "")

    return answer


def cstdform(xcoord, ycoord, radius):
    try:
        xcoord = - float(xcoord)
        ycoord = -float(ycoord)
        radius = (float(radius))**2
    except:
        answer = 'Nope'
        return answer


    if '-' in str(xcoord):
        xcoord = ' - ' + str(xcoord)[1:]
    else:
        xcoord = ' + ' + str(xcoord)

    if '-' in str(ycoord):
        ycoord = ' - ' + str(ycoord)[1:]
    else:
        ycoord = ' + ' + str(ycoord)

    if xcoord[-2:] == '.0':
        xcoord = xcoord[0:-2]
    
    if ycoord[-2:] == '.0':
        ycoord = ycoord[0:-2]

    if str(radius)[-2:] == '.0':
        radius = str(radius)[0:-2]

    answer = f'(x{xcoord})^2 + (y{ycoord})^2 = {radius}'
    return answer


def findx(function):
    f = cleanfunction(function)
    x = Symbol('x')

    return solve(f, x)

# f = 'x^2 - 6x + 9'
# print(findx(f))

# x = Symbol('x')
# y = Symbol('y')
# print(expand(x**2 + 6*x))

print(cstdform(2, -5, 3))