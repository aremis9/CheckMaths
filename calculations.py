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
    answer = answer[1:len(answer) - 1]
    return answer



# func = 'x^2 + 6x + 9 + a'
# 2^(2a) = 2^(4) = 16
# 2^2a = (2^2)*a = (2^2)*2 = 8
# -(4^-3)
func = '2x + x^3 + xy(x + 1) + xy(3) / 2'
# 4 + 8 + 12 + 12 / 2
# func = '4t'
variables = {
    'x': '3',
    'a': '2'
}


print(evaluate(func, variables))
