import json
def Rate():
    filename = 'RbzRate.json'
    with open(filename) as read_file:
        Rbz_rate = json.load(read_file)
    print(f'\nDo you Want To Change The Exsting RB ZRATE which is ${str(Rbz_rate)}0')
    changeRate =input(''' 1. Yes  2. No  : ''' )
    if changeRate == '1':
        Rbz_rate = float(input('Enter Rbz Rate to use: '))
        with open(filename, 'w') as write_file:
            json.dump(Rbz_rate, write_file)
    elif changeRate == '2':
        pass

    return Rate