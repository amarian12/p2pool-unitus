from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    unitus_yescrypt=math.Object(
        PARENT=networks.nets['unitus_yescrypt'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=10, # shares
        SPREAD=30, # blocks
        IDENTIFIER='60e7e29bc82c60e7'.decode('hex'),
        PREFIX='0ee8ca7f6c700ee8'.decode('hex'),
        P2P_PORT=33333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//10000 - 1,
        PERSIST=False,
        WORKER_PORT=22222,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-uis',
        VERSION_CHECK=lambda v: True,
    ),
    unitus_argon2d=math.Object(
        PARENT=networks.nets['unitus_argon2d'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=10, # shares
        SPREAD=30, # blocks
        IDENTIFIER='2c60e7e6d16318fc'.decode('hex'),
        PREFIX='2c60e79a59fbabfe'.decode('hex'),
        P2P_PORT=33334,
        MIN_TARGET=0,
        MAX_TARGET=2**256//10000 - 1,
        PERSIST=False,
        WORKER_PORT=22223,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-uis',
        VERSION_CHECK=lambda v: True,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
