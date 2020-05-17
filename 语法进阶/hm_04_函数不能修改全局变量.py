# 全部变量
num = 10


# 两个函数都可以使用全局变量num
def demo1():
    # 希望在demo1()修改全局变量
    # 这样在demo2()输出的num应该就是修改后的值
    # 但是不是,在Python中,是不允许直接修改全局变量的值的
    # 如果使用赋值语句,会在函数内部定义一个同名的局部变量
    num = 99
    print("demo1 => %s" % num)

def demo2():
    print("demo2 => %s" % num)

demo1()
demo2()