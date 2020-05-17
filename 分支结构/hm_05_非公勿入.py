is_employee = False

# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用 not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也可以使用not
if not is_employee:
    print('非本公司人员， 请勿入内')