hello_str = "hello world"

# 1. 检查字符串是否是以 str 开头，是则返回 True
print(hello_str.startswith("hell"))

# 2.检查字符串是否是以 str 结束，是则返回 True
print(hello_str.endswith("rld"))

# 3.检测 str 是否包含在 string 中，如果 start 和 end 指定范围，则检查是否包含在指定范围内，
#   如果是返回开始的索引值，否则返回 -1
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4.把 string 中的 old_str 替换成 new_str，如果 num 指定，则替换不超过 num 次
print(hello_str.replace("world", "python"))
print(hello_str)
