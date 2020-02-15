# -*- coding: utf-8 -*-
import time
import requests
import schedule


def record():
    url = 'http://m.hlgnet.com/act/dengji/save_everyday_ajax.php'

    data = {
        "unionid": "oVFxp09SLEytXNP-sNH76z0JT6UY",
        "temperature": "36.5",
        "cid0": "2"
    }
    response = requests.post(url, data=data)

    print response.content


if __name__ == '__main__':
    schedule.every().day.at("9:30").do(record())
    schedule.every().day.at("18:30").do(record())
    while True:
        schedule.run_pending()
        time.sleep(1)

