import json

import requests

from src.plugins import PluginManager
from lib.conf.config import settings


class Base(object):

    @staticmethod
    def get_host():
        """获取采集主机IP信息"""
        response = requests.get(settings.API)
        result = json.loads(response.text)
        if not result["status"]:
            return
        return result["data"]

    @staticmethod
    def post_asset(server_info):
        """提交获取到的资产信息"""
        requests.post(settings.API, json=server_info)


class Agent(Base):

    def execute(self):
        pass


class SSHSALT(Base):
    """ssh 连接方式"""

    def run(self, host):
        server_info = PluginManager(host).exec_plugin()
        self.post_asset(server_info)

    def execute(self):
        from concurrent.futures import ThreadPoolExecutor
        host_list = self.get_host()
        pool = ThreadPoolExecutor(10)
        for host in host_list:
            pool.submit(self.run, host)


class Ansible(Base):
    """功过ansible 连接远程主机"""

    def run(self, host):
        server_info = PluginManager(host).exec_plugin()
        self.post_asset(server_info)

    def execute(self):
        from concurrent.futures import ThreadPoolExecutor
        host_list = self.get_host()
        pool = ThreadPoolExecutor(10)
        for host in host_list:
            pool.submit(self.run, host)
