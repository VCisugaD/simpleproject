import re
import random
import requests


# 判断字符串是否为中文，筛选需要的新闻标题
def isChinese(str):
    for ch in str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    else:
        return False


# 爬取数据
def newSpider():  # newstext 爬取到的数据文本内容
    '''
    企业风采 : 'http://www.zqcn.com.cn/260/',
    企业新闻 : 'http://www.zqcn.com.cn/qyxw/index.html',
    宏观经济 : 'http://www.zqcn.com.cn/114/',
    营业环境 : 'http://www.zqcn.com.cn/112/',
    企业文化 : 'http://www.zqcn.com.cn/121/',
    企业之家 : 'http://www.zqcn.com.cn/124/',
    企业管理 : 'http://www.zqcn.com.cn/246/',
    企业党建 : 'http://www.zqcn.com.cn/113/',
    产业经济 : 'http://www.zqcn.com.cn/115/',
    涉企政策 : 'http://www.zqcn.com.cn/257/',
    政商关系 : 'http://www.zqcn.com.cn/259/',
    峰会论坛 : 'http://www.zqcn.com.cn/272/index.html',
    一带一路 : 'http://www.zqcn.com.cn/117/',
    园区建设 : 'http://www.zqcn.com.cn/119/',
    大学堂   : 'http://www.zqcn.com.cn/120/',
    涉企法规 : 'http://www.zqcn.com.cn/258/',
    500强要闻 : 'http://www.zqcn.com.cn/581/',
    500强排行 : 'http://www.zqcn.com.cn/582/',
    500强文化 : 'http://www.zqcn.com.cn/583/',
    500强故事 : 'http://www.zqcn.com.cn/584/',
    500强分析 : 'http://www.zqcn.com.cn/585/',
    主题论坛 : 'http://www.zqcn.com.cn/586/',
    平行论坛 : 'http://www.zqcn.com.cn/587/',
    美丽中国 : 'http://www.zqcn.com.cn/913/'
    '''
    url_ls = ['http://www.zqcn.com.cn/260/', 'http://www.zqcn.com.cn/qyxw/index.html', 'http://www.zqcn.com.cn/114/',
              'http://www.zqcn.com.cn/112/',
              'http://www.zqcn.com.cn/121/', 'http://www.zqcn.com.cn/124/', 'http://www.zqcn.com.cn/246/',
              'http://www.zqcn.com.cn/113/',
              'http://www.zqcn.com.cn/115/', 'http://www.zqcn.com.cn/257/', 'http://www.zqcn.com.cn/259/',
              'http://www.zqcn.com.cn/272/index.html',
              'http://www.zqcn.com.cn/117/', 'http://www.zqcn.com.cn/119/', 'http://www.zqcn.com.cn/120/',
              'http://www.zqcn.com.cn/258/',
              'http://www.zqcn.com.cn/581/', 'http://www.zqcn.com.cn/582/', 'http://www.zqcn.com.cn/583/',
              'http://www.zqcn.com.cn/584/',
              'http://www.zqcn.com.cn/585/', 'http://www.zqcn.com.cn/586/', 'http://www.zqcn.com.cn/587/',
              'http://www.zqcn.com.cn/913/']
    headers_ua = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44']
    headers = {
        'User-Agent': '',
        'Cookie': 'Hm_lvt_b2d32dbc529d46f8e5e1180fd6c011af=1655879579,1655886982,1655945847,1655949864; Hm_lpvt_b2d32dbc529d46f8e5e1180fd6c011af=1655950275',
        'Host': 'www.zqcn.com.cn'
        # 'Referer': 'http://www.zqcn.com.cn/582/'
    }
    # 标签，信息分类
    labels = ['企业风采', '企业新闻', '宏观经济', '营业环境', '企业文化', '企业之家', '企业管理', '企业党建',
              '产业经济', '涉企政策', '政商关系', '峰会论坛', '一带一路', '园区建设', '大学堂', '涉企法规',
              '500强要闻', '500强排行', '500强文化', '500强故事', '500强分析', '主题论坛', '平行论坛', '美丽中国']
    data = []  # 存放所有的数据
    headers['User-Agent'] = random.choice(headers_ua)
    for url in range(len(url_ls)):
        r = requests.get(url_ls[url], headers=headers, timeout=30)
        r.encoding = 'utf-8'  # 解码方式
        if r.status_code == requests.status_codes.codes.OK:
            # 数据中有很多 \n 默认不匹配，可能会导致返回空匹配不到想要的结果，所以要设置re.S 使 . 匹配包括换行在内的所有字符
            pattern = re.compile('<a href="/.*?_blank">(.*?)</a>', re.S)
            txts = pattern.findall(r.text)

            # http://www.zqcn.com.cn/268/11605.html
            pattern_acon = re.compile('<dd class="smlt">(.*?)<a href="(.*?)".*?<dd class="time">(.*?)</dd>', re.S)
            txts_acon = pattern_acon.findall(r.text)  # 匹配内容、链接、时间
            ls = []  # 存放标题

            for i in range(len(txts)):

                if isChinese(txts[i]) == True and txts[i] not in ['注册', '登录']:
                    ls.append(txts[i])

            for k in range(len(txts_acon)):
                dic = {'title': '', 'content': '', 'link': '', 'time': '', 'label': ''}
                dic['title'] = ls[k]
                dic['content'] = re.sub('\s|[\u200b]', '', txts_acon[k][0])  # 清洗内容
                dic['link'] = 'http://www.zqcn.com.cn' + txts_acon[k][1]
                dic['time'] = txts_acon[k][2]
                dic['label'] = labels[url]
                data.append(dic)
        else:
            continue
    return data


# data = newSpider()

if __name__ == '__main__':
    newSpider()
