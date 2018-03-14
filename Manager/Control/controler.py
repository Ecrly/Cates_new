# 用于控制爬虫调度
import os
import redis
import subprocess
import time
from Manager.Models.Spider import SpiderObject
from ..Models.spider_template import template

class Controler():

    # 初始化，同步数据库中的爬虫列表
    def __init__(self):
        self._spider_list = []
        self._spider_obj = {}
        self._spider_process = {}

    # 根据表单中的数据创建爬虫对象
    def _create_spider(self, **kwargs):

        # 初始化爬虫参数
        name = kwargs['name']
        domain = kwargs['domain']
        urls = kwargs['urls']
        rules = kwargs['rules']
        title = kwargs['title']

        # 根据模板生成爬虫文件
        temp = template % (name, domain, urls, rules, title, name, name)
        cwd = os.getcwd()[0:-11]
        print(os.getcwd())
        cwd = cwd + 'Mstx_Spider/spiders'
        if not os.path.exists(cwd):
            os.mkdir(cwd)
        file = cwd + '/Spider_' + name + '.py'
        with open(file, 'w') as f:
            f.write(temp)
        spider = SpiderObject(name=name, status='READY', file=file)
        self._spider_list.append(name)
        self._spider_obj[name] = spider

    # 运行爬虫
    def _start_spider(self, name):
        spider = self._spider_obj[name]
        print("+++++++++++++start")
        # 验证爬虫状态
        if spider.get_status() != 'READY':
            raise Exception('Not READY')
        spider.set_status('RUNING')

        # 创建新进程运行爬虫
        file = spider.get_file()
        name = spider.get_name()
        print(name)
        # file = "C:\www\Scrapy\Cates\Mstx_Spider\start_msj.py"
        print(file)
        process = subprocess.Popen(['python', file])
        if process.returncode != None:
            raise Exception('创建进程失败！')
        print(process)
        self._spider_process[name] = process


    # 停止爬虫
    def _stop_spider(self, name):
        spider = self._spider_obj[name]
        # 验证爬虫状态
        if spider.get_status() != 'RUNING':
            raise Exception('Not RUNING')
        spider.set_status('READY')

        # 杀死该爬虫进程
        process = self._spider_process[name]
        print(process.pid)
        process.kill()
        print(name, 'kill')
        del self._spider_process[name]
        print(process.returncode)

    # 删除爬虫
    def _delete_spider(self, name):
        spider = self._spider_obj[name]

        status = spider.get_status()
        if status == 'READY':
            self._spider_list.remove(name)
        elif status == 'RUNING':
            self._stop_spider(name)
            self._spider_list.remove(name)
            del self._spider_obj[name]

    def _get_spider_list(self):
        data = []
        for sname in self._spider_list:
            dict = {}
            dict['name'] = sname
            dict['status'] = self._spider_obj[sname].get_status()
            if dict['status'] == 'READY':
                dict['pid'] = None
            else:
                dict['pid'] = self._spider_process[sname].pid
            print(dict['pid'])
            data.append(dict)
        print(data)
        return data


    def _get_process(self, sname):
        print(type(self._spider_process[sname]))
        return self._spider_process[sname]


    def _pause_spider(self, sname):
        process = self._spider_process[sname]
        print(process.stdout)
        print((process.pid))

    def run(self):
        self._create_spider()
        self._get_process('')



# controler = Controler()
# controler._start_spider('test8')
# while True:
#     pass