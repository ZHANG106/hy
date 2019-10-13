from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from sqlalchemy import create_engine

# 申明需要用到的全局变量

# 创建连接数据库的引擎，根据需要修改配置
engine = create_engine('mysql+pymysql://root:monnom@106.52.110.228/tp?charset=utf8')

# 首先定义待爬取的页面主链接Boss直聘网
main_url = 'https://www.zhipin.com/'

"""
在“职位”tab下，“热门城市”选择“全国”，再分别选择“融资阶段”在“天使轮”以及“A 轮”，
“公司规模”在“0-20 人”以及“20-99 人”，叉乘出四种可能性,抓取4个url并定义输出文件的文件名
元组形式存储在to_catch这个list里
"""
to_catch = [('%sc100010000/s_301-t_803/' % main_url, '全国_天使轮0-20人'),
            ('%sc100010000/s_301-t_802/' % main_url, '全国_A轮0-20人'),
            ('%sc100010000/s_302-t_803/' % main_url, '全国_天使轮20-99人'),
            ('%sc100010000/s_302-t_802/' % main_url, '全国_A轮20-99')]

# Boss 直聘网注册登录之后才能显示公司和职位的完整信息，所以需要程序模拟登陆的状态，需要cookie，Cookie为抓取到的原始数据
Cookie = 'lastCity=101020100; _uab_collina=156095501054476272944517; sid=sem_pz_bdpc_dasou_title; __c=1561036753; toUrl=https%3A%2F%2Fwww.zhipin.com%2F; t=oG6RP5XK9hqCcRYh; wt=oG6RP5XK9hqCcRYh; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2Fgeek%2Fnew%2Findex%2Frecommend&r=https%3A%2F%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1560955011,1560956262,1561036753,1561037150; __a=25754358.1560955011.1560956253.1561036753.151.3.15.9; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1561037379'

# 将Cookie转换为字典，方便之后加入网络请求中
cookies = {i.split("=")[0]: i.split("=")[1] for i in Cookie.split(";")}
# 为了模拟登陆状态，抓取Chrome浏览器正常访问网站时的请求头
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
}
# 使用requests的session方法来模拟一个登陆状态
sess = requests.session()


def company_finder(catch_lis):
    """
    爬取并解析htlm的主要功能函数，对传入的list中的url，爬取每个url下前20页的公司信息，
    具体包括保存'公司名称', '公司简介', '成立时间', '高管名称', '高管职位', '招聘情况'五个字段，然后到本地csv文件里。
    :param to_catch: 由格式化的元组组成的list，每个元组含有两个元素，第一个是待爬取的url，第二个是要输出的文件名
    :return:
    """
    # 遍历to_catch列表
    for es, file_name in catch_lis:
        # 存储待输出结果的list
        export = []
        # 遍历前20页
        for eachpage in range(1, 21):
            # 拼接出每一页的url
            meta_url = es + '?page=%d&ka=page-%d' % (eachpage, eachpage)
            # 用session.sess的get方法来获取html页面
            res = sess.get(url=meta_url, cookies=cookies, headers=headers)
            # 使用BeautifulSoup解析页面
            soup = BeautifulSoup(res.text, 'lxml')
            # 通过select方法定位h3和a这两个标签，进而找到每个公司的tag组成的list
            recoive = soup.select('h3>a')
            # 生成由每个公司的公司名和公司名链到的href组成的list
            recois = [[i.text, i.attrs.get('href')] for i in recoive]
            # 遍历每个公司的公司名和公司名链到的href组成的list
            for entreprise_name, j in recois:
                # time.sleep(1) #防止访问过于频繁可以使用time函数来降低访问频率
                # 如果公司名对应的链接合法，则进一步的爬取公司的简介页面并解析有效信息
                if j.startswith(r'/gongsi'):
                    try:
                        # 拼接出公司简介页面的url
                        url_en = 'https://www.zhipin.com%s' % j
                        # 用session.sess的get方法来获取html页面
                        entreprise_info = sess.get(url=url_en, cookies=cookies, headers=headers, timeout=3)
                        # 使用BeautifulSoup解析页面
                        s_entre = BeautifulSoup(entreprise_info.text, 'lxml')
                        # 找到名为text的class，这个class在此html中对应公司的简介和高管信息
                        ts = s_entre.select('.text')
                        # 如果有p标签，说明这个页面有公司高管信息，进行提取
                        if ts[0].select('p'):
                            bos_intro = ts[0].select('p')[0].text
                        else:
                            bos_intro = ''
                        # 取到公司简介
                        introduction = ts[-1].text
                        # 取到公司高管或者HR的姓名
                        boss = ts[0].select('a')[0].next
                        # 取到公司高管或者HR的职位
                        position = ts[0].select('a')[0].text[len(boss):-1]
                        # 通过定位标签并切片的方法获取公司成立时间
                        optime = s_entre.select('span[class="t"]')
                        optime_ = optime[2].parent.text[len(optime[2].text):-1]
                        # 将需要输出的结果保存在export列表里
                        export.append(
                            [entreprise_name.strip(), introduction.strip(), optime_, boss.strip(), position.strip(),
                             bos_intro.strip()])
                        # 打印爬取成功的信息
                        print(entreprise_name, '\tOK')
                    # boss直聘网有检测ip反爬虫的机制，如果出现页面异常，很可能是触发了反爬机制，手动进行验证
                    except Exception as e:
                        # 通过input方法来暂停程序，完成验证后输入1继续进行爬取
                        input('出现错误，请登录网站验证ip后输入1继续')
                        print(entreprise_name, '\t跳过')
                        print(repr(e))
        # 使用pandas包输出结构化的csv表格数据到本地
        export = pd.DataFrame(export, columns=['公司名称', '公司简介', '成立时间', '高管名称', '高管职位', '招聘情况'])
        export.to_csv(r'.\result\%s.csv' % file_name, index=False)
        # 使用pandas包的to_sql方法将结果直接存到mysql数据库中
        export.to_sql('boss', con=engine, if_exists='append')


if __name__ == '__main__':
    company_finder(to_catch)
