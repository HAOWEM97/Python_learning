ℹ = 0

while i <10:

    # continue某一条件满足时，不执行后续重复的代码
    if i == 3:
        # 在使用 continue 之前，同样应该修改计数器
        # 否则会出现死循环
        i += 1
        continue

    print(i)

    i += 1