from bitexen_client import API
from bitexen_client.constants import BuySellType, OrderType

def order_book():
    api = API(uri='http://dev.bitexen.com/')
    results = api.get_order_book('BTCTRY')
    print(results)
    return results

def ticker():
    api = API(uri='http://dev.bitexen.com/')
    results = api.get_ticker('BTCTRY')
    print(results)
    return results

def market_info():
    api = API(uri='http://dev.bitexen.com/') #api = API(uri='http://dev.bitexen.com/', key='', secret='', pass_phrase='', username='')
    results = api.get_ticker('BTCTRY')
    print(results)
    return results

def balance():
    api = api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.get_balance()
    print(results)
    return results

def open_orders():
    api = api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.get_open_orders()
    print(results)
    return results

def closed_orders():
    api = api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.get_closed_orders()
    print(results)
    return results

def order_status(order_number=None):
    api = api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.get_order_status(order_number or 0)
    print(results)
    return results

def cancel_order(order_number=None):
    api = api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.cancel_order(order_number or 0)
    print(results)
    return results

def create_order():
    api = api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.create_order('BTCTRY', OrderType.LIMIT_ORDER , BuySellType.BUY , 0.001, price='2000')
    print(results)
    return results


def withdraw_request():
    api = API(uri='http://dev.bitexen.com/', key=None, secret=None, pass_phrase=None, username=None)
    results = api.withdraw_request('XRP', 100.22, 'alias')
    print(results)
    return results
