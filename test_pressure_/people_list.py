# -*- coding:utf-8 -*-
import json
import os

from locust import HttpUser, TaskSet, task, events, between
from common.common import read_yaml
import pytest

@events.test_start.add_listener
def on_test_start(**kwargs):
    print("===测试最开始提醒===")

@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("===测试结束了提示===")


class TestPeopleList(HttpUser):
    """人员列表接口"""
    wait_time = between(1,5)

    def get_config(self):
        config = read_yaml(r'../data/Token.yml')
        config = config['config']
        return config

    def get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.get_config()['token'],
            "PROJECT-HEADER": str(self.get_config()['project_id'])  # 把获取到的当前项目id给到headers
        }
        return headers

    @task(1)
    def test_select_people_list(self):
        """查询人员列表"""
        url = '/v1/console/department/tree'
        res = self.client.get(url=url, headers=self.get_headers())
        assert res.status_code == 200

    @task(1)
    def test_select_project_detail(self):
        """查询项目详情"""
        url = '/v1/project/info/124'
        res = self.client.get(url=url, headers=self.get_headers())
        res_json = res.json()
        assert res_json['data']['id'] == 124

    @task(1)
    def test_console_security(self):
        """查询安全中心"""
        url = '/v1/console/security/distribute'
        res = self.client.get(url=url, headers=self.get_headers())
        # res_json = res.json()
        assert res.status_code == 200

    @task(1)
    def test_console_tongji(self):
        """ 查询主控台安全统计"""
        url = '/v1/console/security/survey'
        res = self.client.get(url=url, headers=self.get_headers())
        res_json = res.json()
        assert res.status_code == 200

    @task(1)
    def test_danger_console(self):
        """主控台危险区域情况"""
        url = '/v1/console/danger/rank'
        res = self.client.get(url=url, headers=self.get_headers())
        res_json = res.json()
        assert res.status_code == 200

    @task(1)
    def test_danger_console_trigger(self):
        url = '/v1/console/security/danger/trigger'
        res = self.client.get(url=url, headers=self.get_headers())
        res_json = res.json()
        assert res.status_code == 200

    def on_start(self):
        pass
        # print('这是SETUP，每次实例化User前都会执行！')

    def on_stop(self):
        pass
        # print('这是TEARDOWN，每次销毁User实例时都会执行！')

class TestKaiyuanLocust(TaskSet):
    # 定义蝗虫对象
    task_set = TestPeopleList
    # 单位毫秒
    min_wait = 3000
    # 单位毫秒
    max_wait = 6000

if __name__ == '__main__':
    # -f : 指定运行的脚本
    # --host: 指定运行项目的host地址
    os.system("locust -f people_list.py --host=http://zah.test.dhwork.cn")