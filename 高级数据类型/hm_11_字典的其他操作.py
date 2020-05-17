xiaoming_dict = {"name":"小明",
                 "age":18}
# 1.统计健值对数量
print(len(xiaoming_dict))

# 2.合并字典
temp_dict = {"gender": True,
            "height": 1.75,
             "age":19}
xiaoming_dict.update(temp_dict)

# 3.清空字典
xiaoming_dict.clear()

print(xiaoming_dict)