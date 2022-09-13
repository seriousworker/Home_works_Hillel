import requests


# get data from the bitpay by API
def get_data() -> list | dict:
    resp = requests.get('https://bitpay.com/api/rates')
    data = resp.json()
    return data


# find requested currency data
def find_data(currency: str) -> dict:
    data = get_data()
    result = {key: val for item in data for (key, val) in item.items() if item['code'] == currency}
    return result
