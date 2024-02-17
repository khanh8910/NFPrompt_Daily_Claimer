from loguru import logger
from web3 import Web3
import random

def claim(private_key):
    web3 = Web3(Web3.HTTPProvider('https://opbnb-mainnet-rpc.bnbchain.org'))
    account = web3.eth.account.from_key(private_key)
    logger.info(f"Start claiming {account.address}")

    tx = {
        "chainId": 204,
        "from": account.address,
        "value": Web3.to_wei(0.0001, 'ether'),
        "nonce": web3.eth.get_transaction_count(account.address),
        "gasPrice": web3.eth.gas_price,
        "to": web3.to_checksum_address('0x3c76649cbae809e18bb577a9e291935f81a00195'),
        "data": "0x2ae3594a"
    }

    tx["gas"] = int(web3.eth.estimate_gas(tx))
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
    return transaction_hash


list_pri = []
with open("private_keys_NFP.txt", 'r', encoding='UTF-8') as f:
    for line in f:
        if line.rstrip() != '':
            list_pri.append(line.rstrip())

#random.shuffle(list_pri)           

for i in list_pri:
    result = claim(i)
    logger.debug(result)
