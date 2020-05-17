xiaoming = {"name": "小明",
            "age": "18",
            "gender": "True",
            "height": "1.75"}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的健值对的key
for k in xiaoming:

    print("%s - %s"% (k, xiaoming[k]))