from datetime import datetime as dt
from pytz import timezone
import requests
from loguru import logger


def get_current_time(tz:str = "Asia/Shanghai", time_format:str = "%Y-%m-%d %H:%M:%S"):
    current_time = dt.now(timezone(tz)).strftime(time_format)
    return current_time


def get_current_date(tz:str = "Asia/Shanghai", date_format:str = "%Y-%m-%d"):
    current_date = dt.now(timezone(tz)).strftime(date_format)
    return current_date

def requests_get(url: str, headers=None, params=None):
    # 发送 GET 请求
    if params is None:
        response = requests.get(url, headers=headers, timeout=(30, 300))
    else:
        response = requests.get(url, params=params, headers=headers, timeout=(30, 300))
    # 检查响应状态
    if response.status_code == 200:
        logger.info("请求成功!")
        # 输出响应内容
        logger.info(response.json())  # 将响应内容解析为 JSON
    else:
        logger.info("请求失败:", response.status_code)


def requests_post(url: str, headers=None, data=None):
    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data, timeout=(30, 300))

    # 检查响应状态
    if response.status_code == 200:
        logger.info("数据已创建!")
        logger.info(response.json())
    else:
        logger.info("请求失败:", response.status_code)
