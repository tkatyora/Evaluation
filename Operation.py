import os
Vat_value = 0.15
productCount = 0
Item = 1
companyName = 'Takudzwa'

def operation(VatOption,quantity,Rbz_rate,products,productCount):
	try:
		if VatOption == '1' or VatOption =='2':
			UnitPrice = float(input('Enter Supplier Unit Price# '))
			if VatOption == '1':
				TotalPrice =   UnitPrice * quantity
				UnitPriceUSD = str(UnitPrice / Rbz_rate)
				TotalPriceUSD = UnitPriceUSD * quantity
				a = str(UnitPriceUSD).split('')[:3]
				print('\nVAT INCLUDED')
				print('Unit Price(ZWL)		 Unit Price(USD)		TotalPrice(ZWL)	')
				print( f'{str(UnitPrice)}0 		  {str(UnitPriceUSD)} 	{str(TotalPrice)}0\n' )
				if products > 1:
					productCount = productCount + 1
			elif VatOption == '2':
				UnitPriceVat =UnitPrice+(UnitPrice * Vat_value) 
				TotalPrice = UnitPriceVat * quantity
				UnitPriceUSD = UnitPriceVat / Rbz_rate
				TotalPriceUSD = TotalPrice / Rbz_rate
				# prices = [['Item','companyName',UnitPrizeVat,UnitPriceUSD,TotalPrice]]
				print('\nVAT EXCLUDED')
				print('Unit Price(ZWL)		 Unit Price(USD)		TotalPrice(ZWL)	')
				print( f'{str(UnitPriceVat)}0 		  {str(UnitPriceUSD)}0 	{str(TotalPrice)}0			' )
		else:
			print(' Invalid Option Selectedd')
	except ValueError:
		print('value-2')

	return operation

