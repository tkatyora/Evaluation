#Mimportimg modules to use 
import os
import math

#Variables 
Vat_value = 0.15
productCount = 0
Item = 1
companyName = 'Takudzwa'

#Actual script
def operation(VatOption,quantity,Rbz_rate,products,productCount):
	try:
		if VatOption == '1' or VatOption =='2':
			UnitPrice = float(input('Enter Supplier Unit Price# '))
			if VatOption == '1':
				TotalPrices =   UnitPrice * quantity
				UnitPriceUSDs = UnitPrice / Rbz_rate
				TotalPriceUSDS = UnitPriceUSDs * quantity
				#Rounding of to 2 decimal Places
				TotalPriceUSD = round(TotalPriceUSDS,2)
				TotalPrice = round(TotalPrices,2)
				UnitPriceUSD = round(UnitPriceUSDs,2)
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
	except Exception as e:
		print(e)

	return operation

