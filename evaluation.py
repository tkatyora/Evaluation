import os
print('Welcome To Telone Evaluation Calculator ')
Rbz_rate = float(input('\nEnter Rbz Rate to use: '))
quantity = int(input('Enter Quantity: '))
Vat_value = 1.15
VatOption = input('''
	      Select VAT option below 
	       1. VAT INCLUDED : 
	       2.VAT EXCLUDED : 
           3.Exit ''')

while True:
		UnitPrice = float(input('Supplier Unit Price: '))
		if VatOption == '1':
			TotalPrice = UnitPrice * quantity
			UnitPriceUSD = UnitPrice / Rbz_rate
			TotalPriceUSD = TotalPrice / Rbz_rate
			print('Unit Price(ZWL) :  Unit Price(USD) : TotalPrice(zwl)')
			print(UnitPriceVat  , UnitPriceUSD , TotalPrice )
		elif VatOption == '2':
			UnitPriceVat = UnitPrice * Vat_value
			TotalPrice = UnitPriceVat * quantity
			UnitPriceUSD = UnitPriceVat / Rbz_rate
			TotalPriceUSD = TotalPrice / Rbz_rate
			print('Unit Price(ZWL) :  Unit Price(USD) : TotalPrice(zwl)')
			print(UnitPriceVat  , UnitPriceUSD , TotalPrice )
		elif VatOption =='3':
			os.sys.Exit()
		else:
			print(' Invalid Option Selected')
      
     
         
  