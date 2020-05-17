name_list = ["zhangsan", "lisi", "wangwu","zhangsan"]

# len(lengh 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中有%d个元素" % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("zhangsan")
print("zhangsan出现了%d次" % count)

name_list.remove("zhangsan")
print(name_list)