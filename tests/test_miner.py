import os
import unittest
from miners.claymore_dual import ClaymoreDual
from core import select_work


class TestMiner(unittest.TestCase):

    def test_miner_slug(self):
        miner = ClaymoreDual()
        self.assertTrue(miner.slug == 'claymore_dual')

    def test_miner_downloads_file(self):
        miner = ClaymoreDual()
        miner.download()

        miner_name = miner.slug

        bitness_dir = os.path.join(os.path.expanduser("~"), '.bitness')
        miner_path = os.path.join(bitness_dir, 'miners/{n}'.format(n=miner_name))

        self.assertTrue(os.path.isdir(miner_path))
        self.assertTrue(os.path.isfile(os.path.join(miner_path, miner.binary)))

    def test_miner_simple_work_execution(self):
        miner, pool, algorithm, parameters, devices = select_work()
        stdout = miner.run(pool, algorithm, parameters, devices)
        self.assertIn('CUDA', stdout)