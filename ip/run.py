from scrapy import cmdline
# import random
# import pyautogui
# import time
#
# for i in range(1, 5):
#     # 设置鼠标移动参数
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     # 在设置范围内移动
#     pyautogui.moveRel(x, y)
#     # 每执行一次，休息10秒，不然太累
#     print(x, y, 'xyxy')
#     time.sleep(5)

cmdline.execute('scrapy crawl ipSpider -o ip.json'.split())
