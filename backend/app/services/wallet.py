from web3 import Web3
from app.config import settings

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{settings.INFURA_ID}'))
account = w3.eth.account.from_key(settings.WALLET_PRIVATE_KEY)

async def execute_trade(signal):
    tx = {
        'to': 'POLYMARKET_CONTRACT_ADDRESS',
        'value': Web3.toWei(signal['fraction'], 'ether'),
        'data': b''
    }
    signed = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {'market_id': signal['market_id'], 'side': signal['side'], 'amount': signal['fraction'], 'price': 1.0}
