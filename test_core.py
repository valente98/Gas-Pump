import el_compa_core

def test_gas_price():
    assert el_compa_core.gas_price('one', 22) == 43.78
    assert el_compa_core.gas_price('two', 10) == 23.70
    assert el_compa_core.gas_price('three', 5) == 14.95

def test_get_gas_type():
    assert el_compa_core.get_gas_type('1') == 'Regular'
    assert el_compa_core.get_gas_type('one') == 'Regular'
    assert el_compa_core.get_gas_type('2') == 'Midgrade'
    assert el_compa_core.get_gas_type('two') == 'Midgrade'
    assert el_compa_core.get_gas_type('3') == 'Premium'
    assert el_compa_core.get_gas_type('three') == 'Premium'

# def test_Keep_log():
#     assert el_compa_core.keep_log(gas,amount,gas_type) == 

def test_revenue_log():
    l = [
        ['a', 'b', 10],
        ['a', 'b', 20],
        ]
    assert el_compa_core.revenue_log(l) == 30
    l = [
        ['a', 'b', 1.1],
        ['a', 'b', 2.2],
        ['a', 'b', 3.3],
        ]
    assert el_compa_core.revenue_log(l) == 6.6
