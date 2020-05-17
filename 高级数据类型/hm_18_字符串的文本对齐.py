# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼",]

for poem_str in poem:
    # print("|%s|" % poem_str.center(10,"　"))
    # print("|%s|" % poem_str.ljust(10, "　"))
    # print("|%s|" % poem_str.rjust(10, "　"))
    # 先用strip方法去除空白字符，再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))