import csv

employees = open('EmployeePay.csv', 'r')

emp_csv_file = csv.reader(employees)

next(emp_csv_file) #skip a row


for rec in emp_csv_file:
    print(f'First Name: {rec[1]}\n')
    print(f'Last Name: {rec[2]}\n')    
    print(f'Salary: ${int(rec[3]):10,.2f}\n')
    bonus = float(rec[3]) * float(rec[4])
    print(f'Bonus: ${bonus:10,.2f} \n')
    total_pay = float(rec[3]) + bonus
    print(f'Total Pay: ${total_pay:10,.2f} \n')
    input()
