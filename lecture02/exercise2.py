house_worked = int(input("Enter your hours_worked :"))
pay_rate = float(input("Enter your pay_rate :"))
gross_pay = house_worked * pay_rate
print("gross_pay :", (house_worked * pay_rate))

total_hours_worked = int(input("Enter yout total_hours_worked :"))
hours_ot = total_hours_worked-house_worked
print("hours_ot:", (total_hours_worked-house_worked))

ot_wages = pay_rate * 1.5 * hours_ot
print("ot_wages:", (pay_rate * 1.5 * hours_ot))

total_wages = ot_wages + gross_pay
print("total_wages:", (ot_wages + gross_pay))