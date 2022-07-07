###
# * @Author: Sereinme
# * @Date: 2022-07-06 16:42:56
# * @LastEditTime: 2022-07-07 19:27:53
# * @LastEditors: Sereinme
# * @Description: GYM reservation main program
# * @FilePath: \GymReserve\main.py
###

import requests
import time
import io
from PIL import Image
from ddddocr import DdddOcr
import re
import reserve
import config
import datetime
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()


@ sched.scheduled_job("cron", day_of_week='*', hour=19, minute=25, second=00)
def GymReserve():
    """
    Main program.
    """
    s = requests.session()
    respose = reserve.login(s)
    place = reserve.select_place(s, config.date, config.gym_id, config.item_id, config.time_session)
    reserve.submit_order(s, place, config.date, config.cost, config.phone)


if __name__ == "__main__":
    try:
        sched.start()
        input()
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()
