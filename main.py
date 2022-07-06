###
# * @Author: Sereinme
# * @Date: 2022-07-06 16:42:56
# * @LastEditTime: 2022-07-06 19:09:38
# * @LastEditors: Sereinme
# * @Description: GYM reservation main program
# * @FilePath: \reserve\main.py
###

import requests
import time
import io
from PIL import Image
from ddddocr import DdddOcr
import re
import requests
import reserve
import config


s = requests.session()
respose = reserve.login(s)
place = reserve.select_place(s, config.date, config.gym_id, config.item_id, config.time_session)
reserve.submit_order(s, place, config.date, config.cost, config.phone)
input()
