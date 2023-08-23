print("Please select opration \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")

op_from = int(input("Select operations from 1, 2, 3, 4 : "))
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))

if op_from == 1 :
    Add = first_number + second_number
    print(first_number, '+' , second_number , '=' , Add)
if op_from == 2 :
    Subtract = first_number - second_number
    print(first_number, '-' , second_number , '=' , Subtract)
elif op_from == 3 :
    Multiply = first_number * second_number
    print(first_number, '*' , second_number , '=' , Multiply)
elif op_from == 4 :
    Divide = first_number / second_number
    print(first_number , '/' , second_number , '=' , Divide)
    
else :
    print("error")