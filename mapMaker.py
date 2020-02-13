from typing import Dict, Any

import selenium as selenium
from pyecharts.charts import Map
from pyecharts import options

from pyecharts.render import make_snapshot
# 使用snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
import requests
name = []
confirmedData = []
deadData = []
cureData = []


def getData():
    apiKey = '1a11a104514835115ead5b12ce597384'
    resp = requests.get(
        'http://api.tianapi.com/txapi/ncovcity/index?key=' + apiKey)
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for i in data_model['newslist']:
        name.append( i['provinceShortName'])
        confirmedData.append(i['confirmedCount'])
        deadData.append(i['deadCount'])
        cureData.append(i['curedCount'])

def makeMap(name, value, maptype, mapName, max):
    data = [list(z) for z in zip(name, value)]
    map1 = Map()
    map1.add(series_name=mapName , data_pair=data, maptype=maptype)
    map1.set_global_opts(visualmap_opts=options.VisualMapOpts(max_= max))
    make_snapshot(snapshot, map1.render(), mapName+".png")

if __name__ == '__main__':
    getData()
    print(confirmedData)
    print(deadData)
    print(cureData)
    makeMap(name, confirmedData, 'china', '中国确诊人数地图',1500)
    makeMap(name, deadData, 'china', '中国死亡人数地图',15)
    makeMap(name, cureData, 'china', '中国治愈人数地图',500)

