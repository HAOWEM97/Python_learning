# 注意：导入工具包时，应该把导入语句放在顶部
# 因为，可以方便下方代码在任何时候使用工具包工具
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入要出的拳 —— 石头（1）／剪刀（2）／布（3）:"))

# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)

print("玩家选择的是 %d ，电脑选择的是 %d" % (player, computer))

# 比较胜负
# 1	石头 胜 剪刀
# 2	剪刀 胜 布
# 3	布 胜 石头
# if () or () or ()
# if( ()
#         or ()
#         or () ):
if (((player == 1) and (computer == 2))
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("恭喜玩家胜利")

# 平局
elif player == computer:
    print("真是心有灵犀，再来一局")

# 败局
else:
    print("恭喜电脑获胜")
