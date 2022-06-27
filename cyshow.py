import sqlite3
import numpy as np
import pandas as pd
from wordcloud import WordCloud


# 清洗数据，获得词云图
def get_cyt():
    con = sqlite3.connect('E:/SQLite/数据库/qydb.db')
    sql = "select * from offers"
    df = pd.read_sql(sql, con)
    data = ''
    for j in range(df['福利'].shape[0]):
        city = str(df['福利'][j])
        if city != np.nan:
            data += city
    # print(data)
    # 词云形状
    # image1 = PIL.Image.open('1.png')
    # MASK = np.array(image1)

    # 绘制词云
    word_cloud = WordCloud(
        font_path="simsun.ttc",
        background_color="white",
        # mask=MASK,                # 指定词云的形状
    )
    word_cloud.generate(data)
    word_cloud.to_file("cyt.png")


if __name__ == '__main__':
    get_cyt()