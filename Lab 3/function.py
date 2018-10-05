def add_(x,y):
    print("The Addition is:",x+y)

def sub_(x,y):
    print("The Addition is:",x-y)

def div_(x,y):
    print("The Addition is:",x*y)

def mul_(x,y):
    print("The Addition is:",x/y)

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter First Number:"))

op = input("Enter The Operation You Want To Perform (+,-,*,/):")

if op == '+':
    add_(num1,num2)
elif op == '-':
    sub_(num1,num2)
elif op == '*':
    mul_(num1,num2)
elif op == '/':
    div_(num1,num2)
