name_list = ["zhangsan", "lisi", "wangwu"]

# 使用迭代遍历列表
"""
每一次循环过程中， 数据都会保存在my_name这个变量中
在循环体内部可以访问到当前这一次获取到的数据
for my_name in 列表变量:
"""
for my_name in name_list:
    print("我的名字叫 %s" % my_name )