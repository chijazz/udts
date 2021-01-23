financial = open("financials.csv", "r")

# headers = financial.readline().split(",")

# print(headers[5])

company = []
company_tax = {}
tax_line = []


for line in financial.readlines():
    company.append(line.split(",")[5])
    specific_company = set(company)
    all_company = list(specific_company)
    all_company.remove("company")
    
financial.seek(0)

for company in all_company:
    
    line_list = []
    
    total = 0
    
    financial.seek(0)
    
    for line in financial.readlines():
        
        if "Amount" not in line and company == line.split(",")[5]:
            
            amount = float(line.split(",")[6])
            
            line_list.append(amount)
            
    total = round(sum(line_list))
            
    company_tax[company] = total
    
financial.close()

for key, value in company_tax.items():
    print(key, value)

# for each company find the sum of tax and put in a dictionary