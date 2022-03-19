# -*- coding:utf-8 -*-

from locust import HttpUser, TaskSet, task, between

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
        res = self.client.get("/index/otn/index12306/getNews", headers= self.headers())
        res_json = res.json()
        assert res.status_code == 200

class WebSite(TaskSet):
    task_set = TestIndex
    min_wait = 1000
    max_wait = 3000

