#!/usr/bin/python3

try:
    import seleniumloader.loader as ld
    ld.Loader.fetch()
except ImportError:
    print("could not load seleniumloader")
    print("won't automatically load selenium drivers")
    pass

from libs.configuration import Configuration
from libs.webdriver import WebDriver
from libs.api import API


class InfoSite(object):
    site = None
    info_endpoint = None

    def __init__(self, site, info_endpoint):
        self.site = site()
        self.info_endpoint = info_endpoint

    def check(self):
        pass


class Informer(object):
    info_sites = []
    sleep_time = 60 * 60  # every hour

    api = None
    config = None

    def __init__(self, config):
        self.api = API()
        self.config = config
        self.driver = WebDriver.build(config)

    def stop(self):
        self.api.stop()


if __name__ == '__main__':
    c = Configuration.parse()
    # c.headless = True
    i = Informer(c)
