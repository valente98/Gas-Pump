import el_compa_core

def main():
    print('Hello! welcome to El Compa Gasolina.')
    msg = ''' \n Wich type of gass would you like?
    \t1. Regular $1.99\n
    \t2. Midgrade $2.37\n
    \t3. Premium $2.99\n '''
    while True:
        gas = input(msg)
        
        if gas == '1' or gas == '2' or gas == '3' or gas.lower()== 'one' or gas.lower() == 'two' or gas.lower() == 'three':
            break
        else:
            print('Sorry, invalid choice!')
    
    amount = input('How many gallons would you like? ')
    if not amount.strip().isnumeric():
        print('Sorry, invalid choice.')
        return None
    
    gas_type = el_compa_core.get_gas_type(gas)
    if not el_compa_core.take_away(gas_type, amount):
        print('Please come back again!')
        return None
    
    
    print('Your total will be ${:.2f}'.format(el_compa_core.gas_price(gas, amount)))
    el_compa_core.keep_log(gas, amount, gas_type)
    print('Thank you for shopping with us today! Have a nice day!!')

if __name__ == '__main__':
    main()