import imgshow
import matplotlib.pyplot as plt


def again_get_img():
    # pie
    df = imgshow.again_get_data()
    data2 = df.groupby(['学历要求', '最低经验要求'])['index'].count()
    ls = [0.] * data2.shape[0]  # 创建一个值为0，长度与data相等的列表ls
    ls[data2.values.argmin()] = 0.1  # 获取data中最小值的位置索引，将ls中同等位置的值设置为0.1

    data2.name = '不同学历不同经验的要求占比情况'
    data2.plot.pie(
        autopct='%.2f%%',  # 设置百分比显示格式(两位浮点数)
        explode=ls,
        pctdistance=0.7,  # 设置百分比显示的距离，默认0.6
        labeldistance=1.4,  # 设置标签显示的距离，默认1.1
        startangle=90,  # 设置起始位置的角度
        counterclock=True,  # 设置饼图的方向，默认逆时针
        wedgeprops=dict(width=0.6)
    )
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.tight_layout()  # 紧密布局，使标题、文本等完整显示
    plt.savefig('img2.png')
    plt.close()


if __name__ == '__main':
    again_get_img()