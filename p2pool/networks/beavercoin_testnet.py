from p2pool.bitcoin import networks

PARENT = networks.nets['beavercoin_testnet']
SHARE_PERIOD = 4 # seconds
CHAIN_LENGTH = 20*60//3 # shares
REAL_CHAIN_LENGTH = 20*60//3 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '5fc2be2d4f0d6bfb'.decode('hex')
PREFIX = '3f6057a15036f441'.decode('hex')
P2P_PORT = 12338
MIN_TARGET = 2**256//50 - 1
MAX_TARGET = 2**256//50 - 1
PERSIST = False
WORKER_PORT = 12332
BOOTSTRAP_ADDRS = '37.120.160.23'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
