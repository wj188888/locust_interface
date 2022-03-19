# -*- coding:utf-8 -*-

from locust import HttpUser, TaskSet, task, between
from random import randint

'''
1. 实现登录基本功能，输出响应，脚本正确
2. 多用户随机登录： 在doLogin方法里构造随机数据， -LR： 参数化 Jmeter： 参数化
3. 添加初始化方法on_start: 类似于构造方法，每个用户只运行一次；
4. 添加检查点。（断言）
- 在请求方法中设置catch_response参数设置成 True
- 调用success或failure方法标注成功或失败
5. 
'''

# 任务类
class TestIndex(HttpUser):
    wait_time = between(1, 5)
    def headers(self):
        headers = {
            "Cookie": "JSESSIONID=E3A734B5A30B986AFCC4BB20D9D050DA; BIGipServerpool_index=787481098.43286.0000; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1106248202.50210.0000; highContrastMode=defaltMode; guidesStatus=off; cursorStatus=off; RAIL_EXPIRATION=1647946366282; RAIL_DEVICEID=KDLr2rn4hydRzZste_YOhEBLROq38NVVXYyCJHz_6a9SLG--e6QIWH2KXQWVRcy1FBCjq1RMxTy-NXBK3LXxf3My4OEzjTbejws8UX0FHF2VZ1h4__e34HdNrUtmTyfBXNoY0Q9ijo7YOAd1Gnx38CGzBeX7xGp2"

        }
        return headers

    @task(1)
    def getIndex(self):
        res = self.client.get("/index/otn/index12306/getNews", headers= self.headers(), catch_response=True) # catch_response使用无效
        if res.status_code == 200:
            res.success()
        else:
            res.failure("can not getIndex!")


        # if "login-pass" in res.text:
        #     res.success()
        # else:
        #     res.failure("Can not getIndex!")



    # def on_start(self):
    #     # 任务开始前自动执行的
    #     self.loginData = [
    #         {"username": "admin1", "password": "admin12316"},
    #         {"username": "admin2", "password": "admin123426"},
    #         {"username": "admin3", "password": "admin1256"}
    #     ]
    #     print("------on_start______")

    # @task(2)
    def dologin(self):
        ranIndex = randint(1, 1000) % len(self.loginData)
        res = self.client.post(url=url, headers=self.headers(), catch_response=True)

        # 断言
        if "login-pass" in res.text:
            res.success()
        else:
            res.failure("Can not login!")
        print(self.loginData[ranIndex]['username'])
        print(res.text)



class WebSite(TaskSet):
    task_set = TestIndex
    min_wait = 1000
    max_wait = 3000

