import os
import RbzRate
import json
import RbzRate
filename = 'RbzRate.json'
with open(filename) as read_file:
        Rbz_rate = json.load(read_file)
try:
	print('\nWelcome To Telone Evaluation Calculator\nPress any letter to Exit Any Time ')
	RbzRate.Rate()
	
    
	Vat_value = 0.15
	VatOption = input('''
			Select VAT option below 
			1. VAT INCLUDED : 
			2.VAT EXCLUDED : 
			3.Exit ''')

	while True:
			quantity = int(input('Enter Quantity: '))
			UnitPrice = float(input('Supplier Unit Price: '))
			if VatOption == '1':
				TotalPrice =   (UnitPrice * quantity)
				UnitPriceUSD = UnitPrice / Rbz_rate
				TotalPriceUSD = TotalPrice / Rbz_rate
				print('Unit Price(ZWL)		Unit Price(USD)			TotalPrice(zwl)			TotalPrice(USD)\n')
				print( f'{str(UnitPrice)} 			{str(UnitPriceUSD)} 		{str(TotalPrice)} 		{str(TotalPriceUSD)}' )
			elif VatOption == '2':
				UnitPriceVat =UnitPrice+(UnitPrice * Vat_value) 
				TotalPrice = UnitPriceVat * quantity
				UnitPriceUSD = UnitPriceVat / Rbz_rate
				TotalPriceUSD = TotalPrice / Rbz_rate
				print('Unit Price(ZWL)		Unit Price(USD)			TotalPrice(zwl)\n')
				print( f'{str(UnitPriceVat)} 			{str(UnitPriceUSD)} 		{str(TotalPrice)}' )
			elif VatOption =='3':
				os.sys.exit()
			else:
				print(' Invalid Option Selected')
except ValueError:
    print('Thanks for Using This Application')
		
		
			
	