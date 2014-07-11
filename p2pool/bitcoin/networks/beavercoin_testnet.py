import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fcc1b7dc'.decode('hex')
P2P_PORT = 12333
ADDRESS_VERSION = 111
RPC_PORT = 12332
RPC_CHECK = defer.inlineCallbacks(lambda beavercoind: defer.returnValue(
            'litecoinaddress' in (yield beavercoind.rpc_help()) and
            (yield beavercoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'tBVC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BeaverCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BeaverCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.beavercoin'), 'beavercoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://nonexistent-litecoin-testnet-explorer/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://nonexistent-litecoin-testnet-explorer/address/'
TX_EXPLORER_URL_PREFIX = 'http://nonexistent-litecoin-testnet-explorer/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8
