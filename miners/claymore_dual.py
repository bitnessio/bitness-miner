from .base import Miner


class ClaymoreDual(Miner):

    url = 'https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v10.0/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v10.0.-.LINUX.tar.gz'
    binary = 'ethdcrminer64'

    def arguments(self, pool=None, merge_pool=None, devices=None):

        if merge_pool:
            return "-epool {stratum_url} -ewal {login} -epsw {password} -esm 3 -dpool {merge_stratum_url} -dwal {merge_login} -dpsw {merge_password} -dcoin {merge_name} -allpools 1".format(
                stratum_url=pool.url,
                login=pool.login,
                password=pool.password,
                merge_name=merge_pool.algorithm,
                merge_stratum_url=merge_pool.url,
                merge_login=merge_pool.login,
                merge_password=merge_pool.password,
            )
        else:
            return "-epool {statum_url} -ewal {login} -epsw {password} -mode 1 -esm 3 -ftime 10".format(
                statum_url=pool.url,
                login=pool.login,
                password=pool.password,
            )