try:
    def calculator():
        print('Welcome to E36 Calculatror\nPress q to exist')
        while True:
            type = input('Select Option\n1.ADSS 2.Ducted # ')
            distance = float(input('Distance From Nearest Point Of Present(m)# '))
            transport = float(input('Distance From Main Exchange(km) # '))
            if distance <= 5000:
                spacing = 50
            elif distance > 5000 and distance <= 40000:
                spacing = 100
            elif distance > 10000 and distance >= 70000:
                print('Hie')
                # spacing = 100
                # poles = distance / spacing
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
            if type == '1':
                print('\nPoles:',str(poles))
                print('10m Poles:',str(tenpoles))
                print('7.5m Poles:',str(sevenpoles))
                print('2 Slices ')
                print('Deadend set , staywire Preparation ,staywire:',str(tenpoles))
                print('Midspan Set:',str(sevenpoles))
                print(f'Transport\nLorry : {str(lorry)}\nTruck : {str(truck)}\n\n')
            elif type == '2':
                print(f'Transport\nLorry :Truck : {str(truck)}\n\n')

            else:
                print('Invalid Optiom Selected')
                
                
    
        return calculator
except ValueError:
    print('Invalid Option Selected')