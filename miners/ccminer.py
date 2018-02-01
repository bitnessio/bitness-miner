from .base import Miner


class CCMiner(Miner):

    binary = 'ccminer'

    def arguments(self, pool=None, merge_pool=None, devices=None):
        pass


class CCMinerSPHash(CCMiner):
    url = 'https://github.com/bitnessio/releases/ccminer-sphash'


class CCMinerTPruvot(CCMiner):
    url = 'https://github.com/bitnessio/releases/ccminer-tpruvot'
