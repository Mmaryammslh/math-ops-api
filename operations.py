import sys

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def main():
    try:
        num1 = int(sys.argv[1])
        operation = sys.argv[2]
        num2 = int(sys.argv[3])
        if operation == '.':
            print(multiplication(num1, num2), end = '')
        if operation == '/':
            print(division(num1, num2), end = '')
    except:
        print('The input format is not supported...')

if __name__ == "__main__":
    main()
   
    
