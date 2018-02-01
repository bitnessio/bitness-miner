from miners.base import Miner
from pools.base import Pool
from algorithms.base import Algorithm
from core.parameters import Parameters


def select_work():
    """ TODO: implement class or something more intelligent here. Should return a tuple of Miner, Pool, Algo, Parameters
    which is assumed to be the most profitable (or maybe just a timely thing to do) at the moment. For instance, in the
    case of exploratative benchmarking.

    :return:
    """
    return Miner(), Pool(), Algorithm(), Parameters()