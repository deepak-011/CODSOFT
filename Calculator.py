def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
def divide(x,y):        
    if y!=0:
        return x/y
    else:
        print("The division Can't Perform")

first = input("Enter the first number :")
second=input("Enter the second number:")
operator=input("Enter the operator which has to be performed(+,-,*,/):")

first=float(first)
second=float(second)

if operator=="+":
    result =add(first,second)
elif operator=="-":
    result=subtract(first,second)
elif operator=="*":
    result=multiply(first,second)
elif operator=="/":
    result=divide(first,second)
else:
    result="The operator is invalid"
    
print("Result:",result)