
try:
    def VatOptions():
    	VatOption = input('''
Select VAT option below 
1.VAT INCLUDED   2.VAT EXCLUDED 3.EXIT : ''')
    	return VatOption
except ValueError:
    print('Invalid Option Selected')