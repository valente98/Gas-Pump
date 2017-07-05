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
            message = '{}, {}, ${}'.format(R, amount, price)
    elif gas == '2':
        message = '{}, {}, ${}'.format(M, amount, price)
    elif gas == '3':
            message = '{}, {}, ${}'.format(P, amount, price)
    with open('log.txt', 'a') as file:
        file.write(message)
    return None