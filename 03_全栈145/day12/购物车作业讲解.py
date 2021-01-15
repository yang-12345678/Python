x = 1
"""
1.让用户输入金额
2.选择购买的商品加入购物车
3.当商品价格超过自己的金额，提示余额不足
4.让用户输入N结算，输入Q退出
"""
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 50},
    {'name': '火箭', 'price': 250}
]
fei_yong = 0

shop_car = {}  # 键 == 列表的索引  值 == 商品的数量

money = input("请输入您的金额：")

if money.isdigit():
    # 真钱
    while True:
        for i in range(len(goods)):
            print(i + 1, goods[i]['name'], goods[i]["price"])
        # ====================商品展示=====================

        choose = input("请输入你要购买的商品：")

        if choose.isdigit() and 0 < int(choose) <= len(goods):
            # 让用户输入商品序号并判断是不是数字以及在不在正常输入范围内
            int_index = int(choose) - 1
            # 通过用户输入的内容-1货到goods的索引

            if shop_car.get(int_index) is None:
                shop_car[int_index] = 1  # shop_car[0] == 1
            else:
                shop_car[int_index] = shop_car[int_index] + 1
            # ================把商品加入购物车==============
        elif choose.upper() == 'N':
            # 结算      ...==pass
            for i in shop_car:
                fei_yong = fei_yong + shop_car[i] * goods[i]["price"]
            # print(fei_yong)

            if int(money) - fei_yong >= 0:
                ...


        elif choose.upper() == 'Q':
            # 退出
            ...
        else:
            print("您的输入有误！请重新输入：")




else:
    # 假钞
    print("请正确输入！")
