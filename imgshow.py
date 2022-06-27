import re
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def again_get_data():
    # 读取数据
    con_re = sqlite3.connect('E:/SQLite/数据库/qydb.db')
    sql_re = "select * from offers"
    df = pd.read_sql(sql_re,con_re)

    #薪资标准化
    c = re.sub('[千元/及以下万小]|·.*?薪','',','.join(df['薪资'].tolist()))
    c = c.split(',')
    for x in range(len(c)):
        if len(c[x]) != 0:
            if c[x][-1] == '年':
                k = re.findall('(.*?)-',c[x])
                # print(k)
                if k == []:
                    c[x] = round((float(re.findall('(.*?)年',c[x])[0])/12),1)*10000
                else:
                    a = round((float(re.findall('(.*?)-',c[x])[0])/12),1)*10000
                    b = round((float(re.findall('-(.*?)年',c[x])[0])/12),1)*10000
                    c[x] = (a+b)/2
            elif c[x][-1] == '天':
                k = re.findall('(.*?)-',c[x])
                if k == []:
                    c[x] = round((float(re.findall('(.*?)天',c[x])[0])*30),1)
                else:
                    a = round((float(re.findall('(.*?)-',c[x])[0])*30),1)
                    b = round((float(re.findall('-(.*?)天',c[x])[0])*30),1)
                    c[x] = (a+b)/2
            elif c[x][-1] == '时':
                k = re.findall('(.*?)-',c[x])
                if k == []:
                    c[x] = round((float(re.findall('(.*?)时',c[x])[0])*240),1)
                else:
                    a = round((float(re.findall('(.*?)-',c[x])[0])*240),1)
                    b = round((float(re.findall('-(.*?)时',c[x])[0])*240),1)
                    c[x] = (a+b)/2
            else:
                if re.findall('-',c[x]) != []:
                    a = round((float(re.findall('(.*?)-',c[x])[0])/12),1)*10000
                    b = round((float(re.findall('-(.*?)$',c[x])[0])),1)*10000
                    c[x] = (a+b)/2
                else:
                    c[x] = float(c[x])*10000
        else:
            c[x] = 0

    # 城市标准化
    for j in range(df['城市'].shape[0]):
        if len(df.城市[j])>2:
            df.城市[j] = df.城市[j][0:2]

    # 经验标准化
    jys = []
    for jy in df['经验要求']:
        s = re.findall('(.*?)-',jy)
        if s == []:
            jys += [0]
        else:
            jys += s

    c = map(int,c)
    jys = map(int,jys)
    df['money'] = pd.Series(c)
    df['最低经验要求'] = pd.Series(jys)

    return df

def again_get_img():
    # %matplotlib notebook
    df = again_get_data()
    # 绘图数据整理
    data = df.pivot_table('money','城市','学历要求').round(1)
    data1 = df.groupby(['城市'])['money','最低经验要求'].mean().round(0)
    fig, axs = plt.subplots(2,1)
    data.plot.bar(
        ax=axs[1],
        stacked=True,
        width=0.8,
        color=['#fce4ec','#78909c','#76B7B2','#BAB0AC','#FF9DA7'],
        rot = 60
    )
    plt.title('每个城市对不同的学历要求给出的平均薪资')

    data1.plot(ax=axs[0], style=['o-','s--'],sharex=True,title='不同城市的平均薪资和平均要求最低经验年数')
    plt.ylabel('平均薪资')

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.tight_layout()  # 紧密布局，使标题、文本等完整显示

    plt.savefig('img1.png')
    plt.close()

if __name__ == '__main__':
    again_get_img()

