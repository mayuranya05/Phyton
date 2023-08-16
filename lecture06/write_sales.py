def main():
    
    num_day = int(input('For how many days do ' + \
                        'you have sales? ' ))
    
    salse_file = open('sales.txt', 'w')

    for count in range(1, num_day + 1) :

        salse = float(input('Enter the sales for day #' + \
                            str(count) + ': '))
        
        salse_file.write(str(salse) + '\n')

    salse_file.close()
    print('Data written to sales.txt')

main()