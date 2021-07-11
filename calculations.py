from sympy import *

def evaluate(func, variables):
    func = func
    # funclen = [i for i in range(len(func))]
    funclen = len(func)
    i = 0
    while i < funclen:
        # insert '*' for multiplication
        # if a number is beside a variable
        if (func[i]).isnumeric():
            if i == len(func) - 1:
                continue
            if (func[i + 1].isalpha()):
                func = func[:i + 1] + '*' + func[i + 1:]

        # insert '*' for multiplication
        # if a variable is beside another variable
        if (func[i]).isalpha():
            if i == len(func) - 1:
                break
            if (func[i + 1].isalpha()):
                func = func[:i + 1] + '*' + func[i + 1:]


        symbols = ['*', '^', '/', '(', ')', ' ']

        # insert '*' for multiplication
        # if a variable or number is beside a '('
        if func[i] == "(":
            if i == 0:
                continue
            if func[i - 1] not in symbols:
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

    print(func)
    answer = Function('f')(func)

    # substitute the values of the variables to the function
    for v in variables.keys():
        # v = variable, variables[v] = value of variable
        answer = answer.subs(v, variables[v])

    return answer



# func = '2x + x^3 + xy(x + 1)'
func = '2x + x^3 + xy(x + 1) + xy(3)'
variables = {
    'x': '2',
    'y': '2'
}

# print(simplify(func))
print(evaluate(func, variables))