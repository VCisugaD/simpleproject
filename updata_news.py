import sqlite3
import pandas as pd
import spider_news


# 更新数据，同时保证没有重复数据
def AddisOnly():
    # 判断数据库中是否有数据
    con = sqlite3.connect('E:/SQLite/数据库/qydb.db')  # 参数：路径+库名 连接该库，若无新建，有就连接
    cur = con.cursor()
    sql_be = "select * from news"
    cur.execute(sql_be)
    be = cur.fetchall()

    # data : 增加的新数据（字典类型）
    data = spider_news.newSpider()
    df2 = pd.DataFrame(data)

    if be == []:
        df2.index = df2.index + 1001
        df2.to_sql('news', con, if_exists='replace')
        return '更新完毕'
    else:
        sql = "select * from news"
        df = pd.read_sql(sql, con)  # sql,con 必需的参数

        # 删除index列
        df.drop(axis=1, columns='index', inplace=True)

        # 判断是否相同
        d_list = df['title'].tolist().sort()
        df_list = df2['title'].tolist().sort()
        ft = d_list == df_list
        if ft == True:
            con.close()
            return '没有新的内容，暂不需要更新'
        else:
            # 合并原本数据和新数据，纵向合并，并重新排序
            df_n = pd.concat([df, df2], axis=0, ignore_index=True)
            df_n.index = df_n.index + 1
            # 去重
            df_n.drop_duplicates(inplace=True)

            # 更新数据库
            df_n.to_sql('news', con, if_exists='replace')
            con.close()

            return '更新完毕！'


if __name__ == '__main__':
    AddisOnly()
