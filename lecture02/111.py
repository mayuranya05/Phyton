hours_worked = int(input("Input the hours worked: "))
houely_pay_rate = float(input("Input the hourly pay rate: "))
x = hours_worked * houely_pay_rate

print("Grosspay: ", format(x, "12,.2f"))