from replit import clear

def add(a,b):
    summation = a + b
    return summation

def minus(a,b):
    subtraction = a - b
    return subtraction

def multiply(a,b):
    multiplication = a*b
    return multiplication

def divide(a,b):
    dividents = a/b
    return dividents

def main():
    continueProgram = True
    
    
    

    while continueProgram is True:
        a = int(input('What is the first number? \n'))
        continueOperation = True
        while continueOperation is True:
            operation = input('please specify your operation, + for plus, - for minus, * for multiplication and / for dividing \n')
            b = int(input('what is the next number? \n'))

            if operation == "+":
                result = add(a,b)
            elif operation == "-":
                result = minus(a,b)
            elif operation == "*":
                result = multiply(a,b)
            elif operation == "/":
                result = divide(a,b)
            
            print('Your operation of {} {} {} got the following result: {} \n'.format(a,operation,b,result))
            userOpinion = input("Plese Type 'y' to continue calculation or 's' to start new program or 'n' to end it \n")
            if userOpinion.lower() ==  'y':
                a = result
            elif userOpinion.lower() == 's':
                continueOperation = False
                clear()
            elif userOpinion.lower() == 'n':
                continueOperation = False
                continueProgram = False


if __name__ == "__main__":
    main()