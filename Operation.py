Vat_value = 0.15
productCount = 0
try:
	def operation(VatOption,quantity,Rbz_rate,products,productCount):
		if VatOption == '1' or VatOption =='2':
			if products > 1:
				quantity = int(input('Enter Quantity: '))	
			UnitPrice = float(input('Enter Supplier Unit Price: '))
			if VatOption == '1':
				print('VAT INCLUDED')
				TotalPrice =   UnitPrice * quantity
				UnitPriceUSD = UnitPrice / Rbz_rate
				TotalPriceUSD = UnitPriceUSD * quantity
				print('Unit Price(ZWL)		 Unit Price(USD)		TotalPrice(zwl)')
				print( f'{str(UnitPrice)}0 		  {str(UnitPriceUSD)}0 	{str(TotalPrice)}0' )
				if products > 1:
					productCount = productCount + 1
			elif VatOption == '2':
				UnitPriceVat =UnitPrice+(UnitPrice * Vat_value) 
				TotalPrice = UnitPriceVat * quantity
				UnitPriceUSD = UnitPriceVat / Rbz_rate
				TotalPriceUSD = TotalPrice / Rbz_rate
				# prices = [['Item','companyName',UnitPrizeVat,UnitPriceUSD,TotalPrice]]
				print('VAT EXCLUDED')
				print('Unit Price(ZWL)		Unit Price(USD)			TotalPrice(zwl)')
				print( f'{str(UnitPriceVat)}0 		{str(UnitPriceUSD)}0 	{str(TotalPrice)}0' )
				if products > 1:
					productCount = productCount + 1
				 
				
		else:
			print(' Invalid Option Selected')

		return operation
except:
	pass
