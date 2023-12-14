import os
import RbzRate
import json
import RbzRate
import Operation
import VatOption
import e36calculator
import getpass


Item = 1
companyName = 'Takudzwa'
pin = 'TelOne2023!'

try:
	filename = 'RbzRate.json'
	Vat_value = 0.15
	productCount =0
	quantity =0
	login_try = 3
	login_count = 0
	print('\nWelcome To Telone Corperates Solutions System\n')
	while login_try > login_count:
		username = input('username$ ')
		password = input('password$ ')
		# password = getpass.getpass(prompt='password$ ')
		if username == companyName and password == pin:
			with open(filename) as read_file:
				Rbz_rate = json.load(read_file)
			calculator = input('''Select Below Options
		1.Qoutaion(E36) Calculator     
		2.Evaluation Calculator
		# ''')
			if calculator == '1':
				Calculator = e36calculator.calculator()
			elif calculator == '2':
				RbzRate.Rate()	
				products = int(input('Number Of Products To be Evaluated# '))
				if products == 1:
					quantity = int(input('Enter Quantity# '))
					while True:
						VatSelection = VatOption.VatOptions()
						if VatSelection == '3':
							print('Thanks for Using This Application')
							os.sys.exit()
						Operation.operation(VatSelection,quantity,Rbz_rate,products,productCount)
				elif products >= 2:
					while True:
						if productCount >= 1:
							productCount=0
							products = int(input('Number Of Products To be Evaluated: '))
						elif productCount == 0:
							VatSelection = VatOption.VatOptions()
							if VatSelection == '3':
								print('Thanks for Using Our Application')
								os.sys.exit()
							while  productCount < products :
								#Operation.operation(VatSelection,quantity,Rbz_rate,products,productCount)
								if VatSelection == '1' or VatSelection == '2':
									quantity = int(input('Enter Quantity# '))
									UnitPrice = float(input('Supplier Unit Price# '))
									if VatSelection == '1':
										TotalPrices =   (UnitPrice * quantity)
										UnitPriceUSDs = UnitPrice / Rbz_rate
										TotalPriceUSDS = TotalPrice / Rbz_rate
										TotalPriceUSD = round(TotalPriceUSDS,2)
										TotalPrice = round(TotalPrices,2)
										UnitPriceUSD = round(UnitPriceUSDs,2)
										print('\nVAT INCLUDED')
										print('Unit Price(ZWL)		 Unit Price(USD)		TotalPrice(ZWL)			')
										print( f'{str(UnitPrice)}0 		  {str(UnitPriceUSD)}0 	{str(TotalPrice)}0\n' )
										
										productCount = productCount + 1
									elif VatSelection == '2':
										UnitPriceVat =UnitPrice+(UnitPrice * Vat_value) 
										TotalPrice = UnitPriceVat * quantity
										UnitPriceUSD = UnitPriceVat / Rbz_rate
										TotalPriceUSD = TotalPrice / Rbz_rate
										# prices = [['Item','companyName',UnitPrizeVat,UnitPriceUSD,TotalPrice]]
										print('\nVAT EXCLUDED')
										print('Unit Price(ZWL)		 Unit Price(USD)		TotalPrice(ZWL)		')
										print( f'{str(UnitPriceVat)}0 		  {str(UnitPriceUSD)}0 	{str(TotalPrice)}0\n' )
										productCount = productCount + 1
								
								else:
									print(' Invalid Option Selected2') 
									break
						else:
							pass
				else:
					print('Sorry Products should Not Be less Than 1!')
							
					# document.save('Financial.docx')	
			else:
				print('You Have Selected Invalid Option')
				os.sys.exit
		else:
			if login_count < 2:
				print('Authentication Failed\n')
				login_count = login_count + 1
			else:
				print('Many Attempts Restart The Application and retry again')
				break
		
except ValueError:
    print('Please Enter Numbers Only\nRe-Run The Program')
except FileNotFoundError:
    print('File Not Found') 
		
		
			
	