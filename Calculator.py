def main():
    num1=float(input('Enter the first number : '))
    num2=float(input('Enter the second number : '))
    opr=input('Enter the operator(+,-,*,/) : ')
    if opr == '+':
       print(f'{num1} + {num2} = {num1+num2}')
    elif opr == '-':
        print(f'{num1} - {num2} = {num1-num2}')
    elif opr == '*':
        print(f'{num1} * {num2} = {num1*num2}')
    elif opr == '/':
        if num2 != 0:
            print(f'{num1} / {num2} = {num1/num2}')
        else:
           print(f'{num1} / {num2} is not defined')
    else :
       print('Invalid entry')

if __name__ == "__main__":
    main()