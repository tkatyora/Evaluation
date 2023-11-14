import json
import os

def Rate():
    try:
        filename = 'RbzRate.json'
        with open(filename) as read_file:
            Rbz_rate = json.load(read_file)
        print(f'\nDo you Want To Change The Exsting RBZ RATE which is ${str(Rbz_rate)}0 ')
        changeRate =input('''1.Yes  2.No  # ''' ).lower()
        if changeRate == 'yes' or changeRate == '1' :
            print(changeRate)
            Rbz_rate = float(input('Enter Rbz Rate to use# '))
            with open(filename, 'w') as write_file:
                json.dump(Rbz_rate, write_file)
        elif changeRate == 'no' or changeRate == '2':
            pass
        else:
            print('You Have Selected an Invalid Option')
            os.sys.exit()
    except ValueError:
        print('RbzRate Should Be Number Only\nRe-Run The Program')
        os.sys.exit()
    except FileNotFoundError:
        print('File Not Found')
        os.sys.exit()

    return Rate



