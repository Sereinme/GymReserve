###
# * @Author: Sereinme
# * @Date: 2022-07-04 17:26:11
# * @LastEditTime: 2022-07-06 16:45:42
# * @LastEditors: Sereinme
# * @Description: Automatically reserve THU gym system python script
# * @FilePath: \reserve\reserve.py
###

import requests
import config
import io
from PIL import Image
from ddddocr import DdddOcr
import re


def login(session):
    """
    Log in gym website
    """
    login_url = 'http://50.tsinghua.edu.cn/j_spring_security_check'

    # input name
    login_post_data = {
        'un': config.usr_id,
        'pw': config.usr_password,
        'x': '58',
        'y': '15'
    }

    post_headers = {
        'Host': '50.tsinghua.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '42',
        'Origin': 'http://50.tsinghua.edu.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://50.tsinghua.edu.cn/userOperation.do?ms=gotoLoginPage',
        'Upgrade-Insecure-Requests': '1'
    }

    r = session.post(url=login_url, data=login_post_data, headers=post_headers)
    return r


def select_place(session, date, gym_id, it_id, time_session):
    """
    Select proper gym place 
    """
    gyms = ["3998000", "4797914", "4836273", "5843934"]
    station = gyms[gym_id]
    url_place = "https://50.tsinghua.edu.cn/gymsite/cacheAction.do?ms=viewBook&gymnasium_id=" + \
        station + "&item_id=" + it_id + "&time_date=" + date + "&userType=1"
    g = session.get(url=url_place)
    place = []
    for line in g.content.decode("gbk").split("\n"):
        line = str(line.strip())
        if line.find(time_session) != -1:
            p = re.findall(r"id:\'(.*?)\',time_session", line)
            place.append(str(p[0]))
    return place


def submit_order(session, place, date, cost, phone):
    """
    Submit reserve permission.
    """
    url_order = "https://50.tsinghua.edu.cn/gymbook/gymbook/gymBookAction.do?ms=saveGymBook"

    for pid in place:
        while True:
            captcha = OCR(session)
            data = {
                'bookData.totalCost': cost,
                'bookData.book_person_zjh': '',
                'bookData.book_person_name': '',
                'bookData.book_person_phone': phone,
                'bookData.book_mode': 'from-phone',
                'item_idForCache': pid,
                'time_dateForCache': date,
                'userTypeNumForCache': '1',
                'putongRes': 'putongRes',
                'code': captcha,
                'selectedPayWay': 0,  # 0 为现场支付，1 为线上支付
                'allFieldTime': pid + '#' + date
            }
            rp = session.post(url_order, data)

            if rp.content.decode("gbk").find("成功") != -1:
                print("预约成功!")
                return
            if rp.content.decode("gbk").find("预定失败：场地已经被预定") != -1:
                break

    print("预约失败!")


def OCR(session):
    """
    OCR recognize captcha code.
    """
    _ocr = DdddOcr(show_ad=False)
    while True:
        captcha_url = "https://50.tsinghua.edu.cn/Kaptcha.jpg"
        ri = session.get(url=captcha_url)
        img = Image.open(io.BytesIO(ri.content))
        cropped = img
        res = _ocr.classification(ri.content)
        res = captcha_judge(res)
        if len(res) == 4:
            break
    return res


def captcha_judge(res):
    """
    Delete irregular character from captcha recognized.
    """
    for x in res:
        if x < "0" or "9" < x < "A" or "Z" < x < "a" or x > "z":
            res = res.strip(x)
    return res
