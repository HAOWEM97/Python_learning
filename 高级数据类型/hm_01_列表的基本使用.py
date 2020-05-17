name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
print(name_list[2])
# 取索引是已知列表内容，想知道位置
print(name_list.index("wangwu"))

# 2. 修改
name_list[1] = "zhaoliu"

# 3. 增加
name_list.append("王小二")
name_list.insert(1, "zhaowu")

temp_list = ["孙长老", "董王", "薛定谔"]
name_list.extend(temp_list)

# 4.删除
name_list.remove("wangwu")
name_list.pop()
name_list.pop(3)
name_list.clear()

print(name_list)