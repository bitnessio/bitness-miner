import os
import urllib
import tarfile
import inflection


class Miner(object):
    """ A base class which represents a specific miner configuration, typically subclasses will specify a url, binary,
    and arguments. These subclasses will be called dynamically via the `select_work` method.

    class ClaymoreDual(Miner):
        url = 'http:// ..'  # url of tar/zip file
        binary = 'ethdcrminer64'  # binary file name to execute within zip
        def arguments(pool, algorithm, parameters, devices):
            return "-epool {statum_url} -ewal {login} -epsw {password} -mode 1 -ftime 10".format(
                statum_url=pool.url,
                worker=pool.login,
                password=pool.password,
                intensity=parameters.intensity,
            )

    miner, pool, merge_pool, devices = select_work()
    miner.run(pool=pool, merge_pool=merge_pool, devices=devices)

    """
    name = None

    def url(self):
        raise NotImplementedError

    def arguments(self, pool, merge_pool, devices):
        raise NotImplementedError

    def download(self):

        urllib.urlretrieve(self.url, self.download_path)

        if (self.download_ext == 'tar.gz'):
            tar = tarfile.open(self.download_path, "r:gz")
            tar.extractall(os.path.join(os.path.dirname(self.download_path), self.slug))
            tar.close()
        elif (self.download_ext == 'tar'):
            tar = tarfile.open(self.download_path, "r:")
            tar.extractall(os.path.join(os.path.dirname(self.download_path), self.slug))
            tar.close()

    def run(self, pool, merge_pool, devices):
        if not self.is_downloaded:
            self.download()

        arguments = self.arguments(pool, merge_pool, devices)

        # run program here
        # return stdout or stream?

    @property
    def is_downloaded(self):
        return os.path.isfile(self.download_path)

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def download_path(self):
        bitness_dir = os.path.join(os.path.expanduser("~"), '.bitness')
        download_dir = os.path.join(bitness_dir, 'miners')
        return os.path.join(download_dir, "{n}.{ext}".format(n=self.slug, ext=self.download_ext))

    @property
    def download_ext(self):
        if self.url.endswith('tar.gz'):
            return 'tar.gz'
        else:
            return self.url[-3:]

    @property
    def slug(self):
        return inflection.underscore(self.name)