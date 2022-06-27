import sqlite3

def offer_lsb(data):
    con = sqlite3.connect('E:/SQLite/数据库/qydb.db')
    data.index = data.index+1
    data.to_sql('offers',con,if_exists='replace')
    print('获取数据成功')
    con.close()

if __name__ == '__main__':
    offer_lsb()