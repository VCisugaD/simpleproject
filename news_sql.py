import sqlite3
import pandas as pd


def qy_sql(key, value, labels):
    '''
    key : 下拉框获取到的文本，判断是时间匹配还是标题匹配
    value : 搜索框输入的内容
    labels : 标签
    '''
    con = sqlite3.connect('E:/SQLite/数据库/qydb.db')
    if labels == [] or labels == '全部':
        if key == '时间':
            sql = "select * from news where time like '%{}%'"
        else:
            sql = "select * from news where title like '%{}%'"
        df = pd.read_sql(sql.format(value), con)

    else:
        df = pd.DataFrame(columns=['index', 'title', 'content', 'time', 'label'])
        for lab in range(len(labels)):
            if key == '时间':
                sql = "select * from news where time like '%{}%' and label = '" + labels[lab] + "'"
            else:
                sql = "select * from news where title like '%{}%' and label = '" + labels[lab] + "'"
            df = df.append(pd.read_sql(sql.format(value), con))
        df.drop_duplicates(inplace=True)  # 去重
        df.sort_values(by='index')  # 按 index 列重新排序
        df.reset_index(drop=True)  # 重新索引

    con.close()
    if value == '' and labels == [] or labels == '全部':
        return df.head(20)
    else:
        return df


if __name__ == '__main__':
    qy_sql()