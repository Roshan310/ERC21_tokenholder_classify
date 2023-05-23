from moralis import evm_api
from pymongo import MongoClient
from utils import get_tier_3_addresses

# ADDRESS = '0x5535a05d89635378e05ba69456ef472f0172b34e'
MORALIS_API_KEY = 'Your API KEY'
CONTRACT = '0x128C1093EAec3b6B49Ec7F6DA18dF0808E93f37b'

tier_3_addresses = get_tier_3_addresses()
print(len(tier_3_addresses))
tier_4_addresses = []

api_key = f'{MORALIS_API_KEY}'

for address in tier_3_addresses:
    params = {
    "address": f"{address}",
    "chain": "polygon",
    "format": "decimal",
    "limit": 100,
    "token_addresses": [],
    "cursor": "",
    "normalizeMetadata": False,
    }
    result = evm_api.nft.get_wallet_nfts(api_key=api_key, params=params)
    final_result = result['result']
    total_nfts = len(final_result)
    if total_nfts >= 1:
        tier_4_addresses.append(address)
        print(address)
    
print(len(tier_4_addresses))

common_address = set(tier_3_addresses) & set(tier_4_addresses)
new_tier_3_addresses = [address for address in tier_3_addresses if address not in common_address]

client = MongoClient('localhost', 27017)
db = client['test']
collection1 = db['tier_3_address']
collection2 = db['tier_4_address']


for data in new_tier_3_addresses:
    collection1.insert_one({'address': data})


for data in tier_4_addresses:
    collection2.insert_one({'address': data})
