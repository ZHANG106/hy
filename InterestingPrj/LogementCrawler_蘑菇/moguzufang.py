import requests
import pandas as pd
from py2neo import Graph, Node

# 最终挖掘到的字段名，分别为房间图片链接，房间街区名称，房间结构，到地铁站的距离，价格，房间细节，其他标签，房间的经纬度坐标
colu_name = ['picture_link', 'title', 'subTitle', 'location', 'showPrice', 'detailDesc', '标签1',
             '标签2',
             '纬度', '经度']
# 抓取到的蘑菇租房的api接口
url = 'https://api.mgzf.com/room-find-web/find/list'
# 连接到neo4j数据库
neo_coon = Graph(
    'http://localhost:7474',
    user='neo4j',
    password='666'
)


def get_logement(stationId=151):
    """
    挖掘租房信息的主函数，通过地铁站的ID和POST请求，得到附近房源的信息，并结构化存储到本地和neo4j数据库中。
    :param stationId: 地铁站对应的ID（以151号金桥路地铁站为例，因为这里房源信息较多且距离学校较近）
    """

    meta = []  # 用来记录信息的list
    # 爬取前25页的租房信息
    for i in range(1, 25):
        # 首先根据抓取到的蘑菇租房app对api接口的访问记录，使用requests.post方法进行模拟
        data = {"stationId": 151, 'serviceVersion': 100, 'currentPage': i, 'cityId': 289}
        res = requests.post(url=url, data=data, verify=False)
        # 因为返回值就是一个结构化的json数据，可以直接进行解析。
        res = res.json()
        # 完全解析json数据，对每一处房源生成包含所有房源信息的二维list，方便生成表格
        result = res["content"]
        label_dic = result['list']
        for j in label_dic:
            labels = j['labels']
            length = len(labels)
            if length > 1:
                label1 = labels[0]['title']
                label2 = labels[1]['title']
            elif length == 1:
                label1 = labels[0]['title']
                label2 = None
            else:
                label1, label2 = None, None
            # 最终的解析到的每一处房源的具体信息
            room_info = [j['pictureUrl'], j['title'], j['subTitle'], j['location'], j['showPrice'],
                         j['detailDesc'], label1, label2, j['lat'], j['lng']]
            meta.append(room_info)
            # 创建房源信息的neo4j的节点并存储
            spit_node = Node('room_object', picture_link=room_info[0], title=room_info[1], subTitle=room_info[2],
                             location=room_info[3], showPrice=room_info[4], detailDesc=room_info[5],
                             label1=room_info[6],
                             label2=room_info[7], lat=room_info[8], lon=room_info[9])
            neo_coon.create(spit_node)
    # 用pandas的to_csv方法存储表格到本地
    dada = pd.DataFrame(meta, columns=colu_name)
    dada.to_csv('.\\%s.csv' % stationId, index=False)


if __name__ == '__main__':
    get_logement(151)
