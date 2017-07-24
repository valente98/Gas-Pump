import el_compa_disk
def gas_price(gas, amount):
    """ str -> Float"""
    if gas == '1' or gas.lower() == 'one':
        return float(amount) * 1.99
    elif gas == '2' or gas.lower() == 'two':
        return round((float(amount) * 2.37), 2)
    elif gas == '3' or gas.lower() == 'three':
        return round((float(amount) * 2.99), 2)
def get_gas_type(gas):
    if gas == '1' or gas.lower() == 'one':
        gas_type = 'Regular'
    elif gas == '2' or gas.lower() == 'two':
        gas_type = 'Midgrade'
    elif gas == '3' or gas.lower() == 'three':
        gas_type = 'Premium'
    return gas_type

def keep_log(gas,amount,gas_type):
    """(str, float) --> str"""
    log = el_compa_disk.help_keep_log(gas,amount,gas_type)
    return log 

def revenue_log(left):
    """return float value of total dollars spent"""
    price = 0
    for item in left:
        price += item[2]
    return price 

def take_away(gas_type, amount):
    str_l = ['type, amount_in_tank, price']
    left = el_compa_disk.in_the_tank()
    for item in left:
        if item[0] == gas_type:
            if float(amount) > (item[1]):
                print('Sorry! We ran out of this type of gas!')
                return False
            else:
                item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file: 
        file.write(message)
    return True
    
def refill():
    str_l = ['type, amount_in_tank, price']
    left = el_compa_disk.in_the_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 10000.0
        item[1]=str(item[1])
        item[2]= str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)  

    with open('tank.txt', 'w') as file:
        file.write(message)