def main():

    num_emps = int(input('How many employee records ' + \
                         'do you want to create? '))
    
    line = num_emps.readline()

    while line != '':

        amount = float(line)

        print(format(amount, '.2f'))