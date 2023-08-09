def main():
    # Get a number from the user.
    number = int(input('Enter a nonnegative integer : '))
    # Get the factorial of the number.
    fact = factorial(number)
    print('The factorial of', number, 'is', fact)
    # Display the factorial.
    
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

main()