import requests
from pymongo import MongoClient
import json

PATH = 'https://api.polygonscan.com/api'
ADDRESS = '0xf57C5d032a0Eb0b9e9a2081F4b7992bed90336D3'
CONTRACT = '0xAe07B360cF41C8971F6c544620A6ed428Ff3a661'
API_KEY = 'VQJKJPPTQDCM8H3YWQ7XNJSI59BHWGGCYQ'
CONVERSION_VALUE = 1000000000000000000


def return_result(url):
    response = requests.get(url)
    result = response.json()
    return result['result']


def get_tier_3_addresses():
    all_data = return_result(f'{PATH}?module=account&action=tokentx&contractaddress={CONTRACT}&address={ADDRESS}&startblock=0&endblock=99999999&page=1&offset=0&sort=asc&apikey={API_KEY}')
    tier_3_addresses = []
    for data in all_data:
        from_address = data['from']
        amount = data['value']
        if int(int(amount)/CONVERSION_VALUE) >= 13333:
            tier_3_addresses.append(from_address)
        else:
            pass
    return tier_3_addresses
