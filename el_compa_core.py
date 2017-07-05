def gas_price(gas, amount):
    """ str -> Float"""
    if gas == '1':
        return float(amount) * 1.99
    elif gas == '2':
        return float(amount) * 2.37
    elif gas == '3':
        return float(amount) * 2.99

def keep_log(gas,amount):
    """(str, float) --> str"""
    price = gas_price(gas,amount)

    message = ''
    if gas == '1':
        gas_type = 'Regular'
    elif gas == '2':
        gas_type = 'Midgrade'
    elif gas == '3':
        gas_type = 'Premium'
    
    message = '\n{}, {}, ${}'.format(gas_type, amount, price)
    with open('log.txt', 'a') as file:
        file.write(message)
    return gas_type

def in_the_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left

def take_away(gas_type, amount):
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[0] == gas_type:
            item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file: 
        file.write(message)