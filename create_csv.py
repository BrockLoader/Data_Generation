from generate_salary import generate_salary
from generate_names import generate_names
from generate_phone_number import generate_phone_number
from generate_address import generate_address
from generate_bsb import generate_bsb
from generate_accountnumber import generate_accountnumber
from generate_emails import generate_emails
from sortable_filename import sortable_filename
import pandas as pd
import secrets as sc

generation_amount = 1000

csvdata = pd.DataFrame()
salaries = pd.DataFrame()
generation_tracker = 100
loop_count = 0


csvdata['FullName'] = generate_names(generation_amount)
acc_nums = generate_accountnumber(generation_amount)
ph_nums = generate_phone_number(generation_amount)

csvdata['Email'] = ""
csvdata['Address'] = ""
csvdata['Salary'] = ""
csvdata['AccountNumber'] = ""
csvdata['AccountName'] = ""
csvdata['BSBNumber'] = ""
csvdata['PhoneNumber'] = ""

for i in range(0, generation_amount):
    csvdata.loc[i]['Email'] = generate_emails(fullname=str(csvdata.iloc[i]['FullName']), domain='loaderhome.me')
    csvdata.loc[i]['Address'] = generate_address()
    csvdata.loc[i]['Salary'] = generate_salary(3000, 25000)
    csvdata.loc[i]['AccountNumber'] = acc_nums.loc[i][0]
    csvdata.loc[i]['AccountName'] = str.replace(csvdata.loc[i]['FullName'], ' ', '_')
    csvdata.loc[i]['BSBNumber'] = generate_bsb()
    csvdata.loc[i]['PhoneNumber'] = ph_nums.loc[i][0]
    loop_count = loop_count + 1
    if loop_count == generation_tracker:
        print(generation_tracker, ' Users Generated')
        generation_tracker = generation_tracker + 100

csvdata.to_csv(sortable_filename('Test', 'csv'))