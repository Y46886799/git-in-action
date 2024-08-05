import requests
from loguru import logger


def requests_get(url: str, headers=None, params=None):
    # 发送 GET 请求
    if params is None:
        response = requests.get(url, headers=headers, timeout=(30, 60*60*4))
    else:
        response = requests.get(url, params=params, headers=headers, timeout=(30, 60*60*4))
    # 检查响应状态
    if response.status_code == 200:
        logger.info("请求成功!")
        # 输出响应内容
        logger.info(response.json())  # 将响应内容解析为 JSON
    else:
        logger.info("请求失败:", response.status_code)


def requests_post(url: str, headers=None, data=None):
    # 发送 POST 请求
    response = requests.post(url, headers=headers, json=data, timeout=(30, 60*60*4))

    # 检查响应状态
    if response.status_code == 200:
        logger.info("数据已创建!")
        logger.info(response.json())
    else:
        logger.info("请求失败:", response.status_code)


if __name__ == "__main__":
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3NTM5NDE2MTIuNjE2OTg4NH0.yCFxWDdynhA2r38uHT-6reIjRS1jhDATWriyKa8Bo90',
        'Content-Type': 'application/json',
    }
    url_prefix = 'http://dreamtown.synology.me:5186'
    logger.info("***Step1:Hello World")
    requests_get(url_prefix, headers)
    logger.info("\n")

    logger.info("***Step2:Download Data")
    requests_get('{}/incremental_download_data'.format(url_prefix), headers)
    logger.info("\n")

    logger.info("***Step3:Download Data Weekend")
    requests_get('{}/incremental_download_data_weekend'.format(url_prefix), headers)
    logger.info("\n")

    logger.info("***Step4:Hello World Again")
    requests_get(url_prefix, headers)
