print('Welcome To Telone Evaluation Calculator ')
Rbz_rate = float(input('\nEnter Rbz Rate to use: '))
Vat_value = 1.15
VatOption = input('''
	      Select VAT option below 
	       1. VAT INCLUDED : 
	       2.VAT EXCLUDED :''')


if VatOption == '1':
    UnitPrice = float(input('Supplier Unit Price: '))
    UnitPriceVat = UnitPrice * Vat_value