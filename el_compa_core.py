def gas_price(gas, amount):
    """ str -> Float"""
    if gas == '1':
        return float(amount) * 1.99
    elif gas == '2':
        return float(amount) * 2.37
    elif gas == '3':
        return float(amount) * 2.99

def keep_log(gas,amount):
    R = 'Regular'
    M = 'Midgrade'
    P = 'Premium'

    price = gas_price(gas,amount)

    message = ''
    if gas == '1':
            message ='\n'+ '{}, {}, ${}'.format(R, amount, price)
    elif gas == '2':
        message = '\n'+'{}, {}, ${}'.format(M, amount, price)
    elif gas == '3':
            message = '\n' +'{}, {}, ${}'.format(P, amount, price)
    with open('log.txt', 'a') as file:
        file.write(message)
    return None

def in_the_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        for line in file:
            split_string = line.split(', ')
            fruits.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left