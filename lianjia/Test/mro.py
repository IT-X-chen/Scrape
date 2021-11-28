# -*- encoding: utf-8 -*-

"""
@File    :   mro.py    
2021/11/27 16:07     Xchen~      
"""


class A(object):
    def __init__(self):
        self.name = "xchen"


data = {'housing': '整租·蓝天星港花园 3室1厅 南', 'location': '江宁-禄口-蓝天星港花园',
        'area': '86.00㎡', 'toward': '南', 'housingNum': '3室1厅1卫', 'conditions': '精装、随时看房', 'average': '2500元/月',
        'detailUrl': 'https://nj.lianjia.com/zufang/NJ2876225443747602432.html',
        'picUrl': 'https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20211123141538671'}
print(list(data.values()))
print("\',\'".join(data.values()))