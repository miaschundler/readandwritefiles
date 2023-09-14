import csv

customers = open('customers.csv', 'r')

customer_csv_file = csv.reader(customers)

next(customer_csv_file) #skip a row

outfile = open('customer_country.csv', 'w')

outfile.write('Full Name, Country \n')

rec_count = 0

for rec in customer_csv_file:
    outfile.write(f'{rec[1]} {rec[2]}, {rec[4]} \n')    
    rec_count = rec_count + 1

outfile.write(f'Total Customer Records: {rec_count}')

outfile.close()
