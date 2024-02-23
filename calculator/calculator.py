def calculator():
    num1=float(input('Enter the first number:\n'))
    dsSDSoperator= input('Enter the operator +,-,*,/ :\n ')
    num2= float(input('Enter the second number:\n '))

    if operator =='+':
        result= num1+num2
    elif operator =='-':
        result =num1-num2
    elif operator == '*':
        result =num1*num2
    elif operator =='/':
            if num2 !=0:
                result =num1/num2
            else:
                print('enter a valid number')
                return
    else:
        print('invalid operator')
        return
    print("Result:", result)
calculator()
