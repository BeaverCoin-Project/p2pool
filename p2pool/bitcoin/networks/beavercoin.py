import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 2333
ADDRESS_VERSION = 25
RPC_PORT = 2332
RPC_CHECK = defer.inlineCallbacks(lambda beavercoind: defer.returnValue(
            'beavercoinaddress' in (yield beavercoind.rpc_help()) and
            not (yield beavercoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'BVC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BeaverCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BeaverCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.beavercoin'), 'beavercoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.litecoin.net/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
