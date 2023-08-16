def main():
    
    num_emps = int(input('How many employee records do you want to create? '))
    
    infile = open('employees.txt', 'r')

    for count in range(1, num_emps + 1) :
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

    num1 = input('Name : ')
    num2 = input('ID number : ')
    num3 = input('Depertment : ')

    infile.write(str(num1) + '\n')
    infile.write(str(num2) + '\n')
    infile.write(str(num3) + '\n')