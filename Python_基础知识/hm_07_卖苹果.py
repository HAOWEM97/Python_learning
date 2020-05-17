# 1.输入苹果单价
price_str = input("price")
price_flo= float(price_str)

# 2.输入苹果重量
weight_str = input("weight")
weight_flo = float(weight_str)
# 3.计算价格

money = (price_flo * weight_flo)
print(money)