import el_compa_core
def main():
    msg = ''' Hello! welcome to El Compa Gasolina. Wich type of gass would you like?
    \t1. Regular $1.99\n
    \t2. Midgrade $2.37\n
    \t3. Premium $2.99\n '''
    while '1' or '2' or '3':
        gas = input(msg)
        if gas == '1':
            amount = input('How much gas would you like? ')
            el_compa_core.keep_log(gas,amount)
            print('Your total will be ${:.2f}'.format(el_compa_core.gas_price(gas, amount)))
            break
        elif gas == '2':
            amount = input('How much gas would you like? ')
            el_compa_core.keep_log(gas,amount)
            print('Your total will be ${:.2f}'.format(el_compa_core.gas_price(gas, amount)))
            break
        elif gas == '3':
            amount = input('How much gas would you like? ')
            el_compa_core.keep_log(gas,amount)
            print('Your total will be ${:.2f}'.format(el_compa_core.gas_price(gas, amount)))
            break
        else:
            print('Sorry, invalid choice!')

    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()

        