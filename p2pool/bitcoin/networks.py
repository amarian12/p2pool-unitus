import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

def get_subsidy(height):
    if height < 17291:
        return 347 * 100000000
    halvings = height // 240000
    if halvings >= 64:
        return 0
    return (50 * 100000000) >> halvings

nets = dict(
    unitus_yescrypt=math.Object(
        P2P_PREFIX='c5abc69d'.decode('hex'),
        P2P_PORT=11111,
        ADDRESS_VERSION=68,
        RPC_PORT=1111,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'unitusaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: get_subsidy(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('yescrypt_hash').getHash(data, 80)),
        BLOCK_PERIOD=300, # s
        SYMBOL='UIS',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'unituscoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/unituscoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.unituscoin'), 'unituscoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.unitus.nutty.one/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.unitus.nutty.one/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.unitus.nutty.one/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//10000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    unitus_argon2d=math.Object(
        P2P_PREFIX='c5abc69d'.decode('hex'),
        P2P_PORT=11112,
        ADDRESS_VERSION=68,
        RPC_PORT=1112,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'unitusaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: get_subsidy(height+1),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('argon2d_hash').getHash(data, 80)),
        BLOCK_PERIOD=300, # s
        SYMBOL='UIS',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'unituscoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/unituscoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.unituscoin'), 'unituscoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.unitus.nutty.one/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.unitus.nutty.one/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.unitus.nutty.one/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//10000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
