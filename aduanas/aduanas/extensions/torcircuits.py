import logging
import os
import signal
import shlex
import subprocess
import time

import scrapy

logger = logging.getLogger(__name__)

class TorCircuits(object):
    def __init__(self, rotate_http_codes):
        self.rotate_http_codes = rotate_http_codes
        self.last_rotate = 0
        self.tor = None
        self.polipo = None

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('TORCIRCUITS_ENABLED'):
            raise scrapy.exceptions.NotConfigured

        # configure http codes to trigger circuit rotation
        rotate_http_codes = set(int(code) for code
                                in crawler.settings.getlist('TORCIRCUITS_ROTATE_HTTP_CODES'))

        extension = cls(rotate_http_codes)

        crawler.signals.connect(extension.spider_opened, signal=scrapy.signals.spider_opened)
        crawler.signals.connect(extension.spider_closed, signal=scrapy.signals.spider_closed)
        crawler.signals.connect(extension.response_received, signal=scrapy.signals.response_received)

        return extension

    def spider_opened(self, spider):
        project_path = os.path.dirname(os.getcwd())
        self.tor = subprocess.Popen(
            shlex.split('tor -f config/tor.conf'),
            cwd=project_path)
        self.polipo = subprocess.Popen(
            shlex.split('polipo -c config/polipo.conf'),
            cwd=project_path)

    def spider_closed(self, spider, reason):
        self.tor.terminate()
        self.polipo.terminate()

    def response_received(self, response, request, spider):
        if response.status in self.rotate_http_codes:
            self.rotate_circuits()

    def rotate_circuits(self):
        if time.time() - self.last_rotate > 30:
            self.rotate = time.time()
            logging.info('Rotating tor circuits at ' + str(int(self.last_rotate)))
            self.tor.send_signal(signal.SIGHUP)
