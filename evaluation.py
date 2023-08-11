import os
from docx import Document
import RbzRate
import json
import RbzRate
Item = 1
companyName = 'Takudzwa'

try:
	filename = 'RbzRate.json'
	with open(filename) as read_file:
		Rbz_rate = json.load(read_file)
	print('\nWelcome To Telone Evaluation Calculator\nPress any letter to Exit Any Time ')
	RbzRate.Rate()
	Vat_value = 0.15
	VatOption = input('''
			Select VAT option below 
			1.VAT INCLUDED : 
			2.VAT EXCLUDED : 
			3.Exit ''')
 
	if VatOption == '3':
		print('Thanks for Using Our Application')
		os.sys.exit()
	while True:
		document = Document()
		if VatOption == '1' or VatOption == '2':
			quantity = int(input('Enter Quantity: '))
			UnitPrice = float(input('Supplier Unit Price: '))
			document.add_heading('5.0 Finincial Evaluation')
			table = document.add_table(rows=6, cols=6)
			table_header = [ 'Item','Company','Quantity','UnitPrizeZWL','UnitUSDPrice','TotalPrice']
			if VatOption == '1':
				TotalPrice =   (UnitPrice * quantity)
				UnitPriceUSD = UnitPrice / Rbz_rate
				TotalPriceUSD = TotalPrice / Rbz_rate
				prices = [[Item,companyName,UnitPrizeZWL,UnitPriceUSD,TotalPrice]]
				for i in range(6):
					hdr_cells = table.rows[0].cells[i].text = table_header[i]
				for  Items,companyName,Quantity,UnitPrizeZWL,UnitUSDPrice,TotalPrice in prices:
						row_cells = table.add_row().cells
						row_cells[0].text = str(Item)
						row_cells[2].text =  str(Quantity)
						row_cells[3].text =str(UnitPrizeZWL)
						row_cells[4].text = str(UnitUSDPrice)
						row_cells[5].text =str(TotalPrice)
						row_cells[1].text = companyName
			
				print('Unit Price(ZWL)		Unit Price(USD)			TotalPrice(zwl)			TotalPrice(USD)\n')
				print( f'{str(UnitPrice)} 			{str(UnitPriceUSD)} 		{str(TotalPrice)} 		{str(TotalPriceUSD)}' )
			elif VatOption == '2':
				UnitPriceVat =UnitPrice+(UnitPrice * Vat_value) 
				TotalPrice = UnitPriceVat * quantity
				UnitPriceUSD = UnitPriceVat / Rbz_rate
				TotalPriceUSD = TotalPrice / Rbz_rate
				# prices = [['Item','companyName',UnitPrizeVat,UnitPriceUSD,TotalPrice]]
				print('3')
				print('Unit Price(ZWL)		Unit Price(USD)			TotalPrice(zwl)\n')
				print( f'{str(UnitPriceVat)} 		{str(UnitPriceUSD)} 	{str(TotalPrice)}' )
		
		else:
			print(' Invalid Option Selected') 
			break
			
		document.save('Financial.docx')		
    
except ValueError:
    print('Thanks for Using This Application')
except FileNotFoundError:
    print('File Not Found') 
		
		
			
	