print('Welcome To Telone Evaluation Calculator ')
Rbz_rate = float(input('\nEnter Rbz Rate to use: '))
quantity = int(input('Enter Quantity: '))
Vat_value = 1.15
VatOption = input('''
	      Select VAT option below 
	       1. VAT INCLUDED : 
	       2.VAT EXCLUDED :''')

while True:
    
	if VatOption == '1': 
		UnitPrice = float(input('Supplier Unit Price: '))
		UnitPriceVat = UnitPrice * Vat_value
		TotalPrice = UnitPrice * quantity
		UnitPriceUSD = UnitPriceVat / Rbz_rate
		TotalPriceUSD = TotalPrice / Rbz_rate
		print('Unit Price(ZWL) :  Unit Price(USD) : ')
  