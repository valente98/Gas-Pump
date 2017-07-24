import el_compa_core
import el_compa_disk
def main():
    gas = input('refuel or revenue: ')
    if gas.lower() == 'refuel':
        el_compa_core.refill()
        print('Tanks refueled.')
        return None
    if gas.lower() == 'revenue':
        left = el_compa_disk.in_the_log()
        print('your total revenue is ${:.2f}'.format(el_compa_core.revenue_log(left)))
        return None
if __name__ == '__main__':
    main()