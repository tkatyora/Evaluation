try:
    def calculator():
        print('Welcome to E36 Calculatror\nPress q to exist')
        while True:
            distance = float(input('Distance From Nearest Point Of Present(m): '))
            transport = float(input('Distance From Main Exchange(km) : '))
            if distance <= 5000:
                spacing = 50
            elif distance > 5000 and distance <= 10000:
                spacing = 70
            elif distance > 10000 and distance >= 70000:
                spacing = 100
            elif distance > 70000:
                print('Distance To Large Requires Radio Link')
            else:
                print('Distance Can Not Be Negative')
            poles = distance / spacing
            tenpoles = poles / 5
            sevenpoles = (poles / 5) * 4
            lorry = transport * 2
            truck = lorry * 5
            print(f'\nDistance : {str(distance)}m')
            print('\nPoles:',str(poles))
            print('10m Poles:',str(tenpoles))
            print('7.5m Poles:',str(sevenpoles))
            print('Deadend set , staywire Preparation ,staywire:',str(tenpoles))
            print('Midspan Set:',str(sevenpoles))
            print(f'Transport\nLorry : {str(lorry)}\nTruck : {str(truck)}')
            
    
        return calculator
except ValueError:
    print('Invalid Option Selected')