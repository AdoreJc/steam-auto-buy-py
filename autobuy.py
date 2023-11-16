from datetime import datetime
import pandas as pd
from steampy.client import SteamClient
from steampy.exceptions import ApiException, TooManyRequests
from steampy.models import Currency, GameOptions
import time

# 设置Steam账户信息
api_key = 'MY_API_KEY'
username = 'MY_USERNAME'
password = 'MY_PASSWORD'
steam_guard = 'PATH_TO_STEAMGUARD_FILE'

# 创建SteamClient对象
steam_client = SteamClient(api_key)

# 物品信息
item_name = '★ Butterfly Knife'  # 替换为你要购买的物品名称
currency = Currency.CNY # 设置货币
max_price = 12.34  # 设置最大购买价格
max_quantity_to_buy = 1  # 设置最大购买数量
quantity = 0 # 购买计数

# 记录成功的订单列表
successful_orders = []

def login_to_steam():
    try:
        steam_client.login(username, password, steam_guard)
        print("Login Success")
        return True
    except Exception as e:
        print(f"Login failed: {e}")
        return False

while not login_to_steam():
    print("Retrying login...")
    time.sleep(20)

# 循环检测并购买
while True:
    try:
        # 检测 session 是否连接
        if not steam_client.is_session_alive:
            while not login_to_steam():
                print("Retrying login...")
                time.sleep(20)

        # 获取物品在市场上的价格
        market_prices = steam_client.market.fetch_price(item_name, GameOptions.CS, currency=currency)
        # market_prices = {'volume': '208', 'lowest_price': '¥ 11.30', 'median_price': '$11.33 USD', 'success': True}

        # 获取最低价格
        lowest_price = market_prices['lowest_price']
        lowest_price = float(lowest_price[2:])

        # 当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if float(lowest_price) <= max_price:
            # 购买数量
            quantity_to_buy = 1

            # 发起购买订单
            price_string = str(int(lowest_price * 100))
            response = steam_client.market.create_buy_order(item_name, price_string, quantity_to_buy, GameOptions.CS,
                                                            currency=currency)
            buy_order_id = response["buy_orderid"]

            # 检查购买订单是否成功
            if buy_order_id:
                print(f"{current_time} 成功购买 {quantity_to_buy} 个 {item_name} 在 ¥ {lowest_price} 。")
                print(f"订单ID: {buy_order_id}")

                # 记录成功的订单信息
                successful_order_info = {
                    "timestamp": current_time,
                    "item_name": item_name,
                    "quantity": quantity_to_buy,
                    "price": lowest_price
                }
                successful_orders.append(successful_order_info)

                # 保存成功的订单信息到 Excel 文件
                df = pd.DataFrame(successful_orders)
                df.to_excel("orders.xlsx", index=False)

                quantity += 1
            else:
                print(f"{current_time} 订单失败")
            time.sleep(3)
        else:
            print(f"{current_time} 当前最低价 ({lowest_price})， 大于目标价格 ({max_price})。")

        # 大于购买数量停止
        if quantity >= max_quantity_to_buy:
            print(f"完成 {max_quantity_to_buy} 个订单采购")

            # 打印成功的订单信息
            print("成功的订单:")
            print(successful_orders)
            print("扫货结束")
            break

        # 建议间隔大于等于3，不然API容易被限制，被限制之后关闭脚本一段时间后再使用即可
        time.sleep(2)

    except TooManyRequests as e:
        print("TooManyRequests: 60s内最多请求20次")
        time.sleep(10)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
