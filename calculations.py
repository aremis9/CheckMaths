from sympy import *
from sympy.geometry.util import find

# import smtplib, ssl
import smtplib
from email.message import EmailMessage
from decouple import config 


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

    if '-' in str(radius):
        answer = 'Radius cannot be negative!'

    if xcoord[-2:] == '.0':
        xcoord = xcoord[0:-2]
    
    if ycoord[-2:] == '.0':
        ycoord = ycoord[0:-2]

    if str(radius)[-2:] == '.0':
        radius = str(radius)[0:-2]

    answer = f'(x{xcoord})^2 + (y{ycoord})^2 = {radius}'
    return answer


def cgrlform(xcoord, ycoord, radius):
    try:
        xcoord = float(xcoord)
        ycoord = float(ycoord)
        radius = float(radius)
    except:
        answer = 'Nope'
        return answer

    stdform = cstdform(xcoord, ycoord, radius)
    stdform = stdform[0:stdform.find('=')] + f'- {radius**2}'
    answer = str(expand(cleanfunction(stdform)))
    answer = answer.replace("**", "^")
    answer = answer.replace("*", "")
    if str(answer)[-2:] == '.0':
        answer = str(answer)[0:-2]
    return answer


def findx(function):
    f = cleanfunction(function)
    x = Symbol('x')
    answer = str(solve(f, x))
    answer = answer.replace("I", "i")
    answer = answer.replace("**", "^")
    answer = answer.replace("*", "")
    return answer


def getlimit(function, c):
    f = cleanfunction(function)
    x = Symbol('x')

    answerp = str(limit(f, x, c, '+'))
    answern = str(limit(f, x, c, '-'))

    if answerp == answern:
        answer = answerp
    else:
        answer = 'none'

    return answer
    

def differentiate(function, nth):
    f = cleanfunction(function)
    x = Symbol('x')
    n = int(nth)
    answer = expand(f)

    for i in range(n):
        answer = diff(answer, x)

    answer = str(answer)
    answer = answer.replace("**", "^")
    answer = answer.replace("*", "")

    return answer


# f = 'x^2 - 6x + 9'
# print(findx(f))

# x = Symbol('x')
# y = Symbol('y')
# print(expand(x**2 + 6*x))

# answer = getlimit("(x + 1)/(Abs(x + 1))", '-1')
# answer = getlimit("(6 + 4x)/(x^2 + 1)", '-3')

# print(answer)


# answer = differentiate('x(3x^2 - 9)', 1)
# print(answer)


# def sendemail():
#     port = 465  # For SSL
#     smtp_server = "smtp.gmail.com"
#     receiver_email = 'kmsimera@gmail.com'  # Enter receiver address
#     sender_email = config('myemail')  # Enter sender address
#     password = config('mypassword') 
#     message = """\
#     Subject: Hi there

#     This message is sent from Python."""

#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)


def sendemail():
    msg = EmailMessage()

    msg['To'] = 'example@email.com'        # receiver
    msg['From'] = config('myemail')           
    email = config('myemail')               # sender email
    password = config('mypassword')         # sender password

    msg['Subject'] = 'Subject'              # subject
    msg.set_content('This is my message')   # message

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email, password)
    server.send_message(msg)
    server.quit()

sendemail()