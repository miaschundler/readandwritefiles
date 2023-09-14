import csv

sales = open('sales.csv', 'r')

sales_csv_file = csv.reader(sales)

next(sales_csv_file) #skip a row

outfile = open('salesreport.csv', 'w')

outfile.write('Customer ID, Total \n')

cust_id= 250
total =0

for rec in sales_csv_file:
    if cust_id == int(rec[0]):
        total += float(rec[3]) + float(rec[4]) + float(rec[5])
    else:    
        outfile.write(f'{cust_id}, {total:.2f} \n') 
        cust_id = cust_id + 1
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
       
outfile.close()
