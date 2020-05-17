def test(num):
    print("在函数内部 %s 对应的 内存地址是 %s " % (num, id(num)))
    # 1> 定义一个字符串变量
    result = "hello"
    print("函数要返回的内存地址是 %s" % id(result))
    # 2> 将字符串变量返回
    return result

# 1. 定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print("a 变量保存数据的内存地址是 %s" % id(a))

# 2. 调用test()函数
# 本质上传递的是实参保存数据的引用,
# 而不是实参保存数据的值

r = test(a)
print("%s 的内存地址是 %s" % (r, id(r)))
