# 在定义全局变量时，有些公司会有一些开发要求，例如：
# 全局变量名前应该增加 g_ 或者 gl_ 的前缀
gl_num = 10
gl_title = "传智 - 黑马"
gl_name = "小明"

def demo():

    # 如果全局变量和局部变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99
    print("%s" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)

demo()