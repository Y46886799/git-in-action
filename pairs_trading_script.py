import requests
from loguru import logger


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


if __name__ == "__main__":
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3NTM2ODIxMzEuNDQ1NzM2Nn0.nHoiPQYeyOg5hnQ3NCgowSp5RHmBbHlSRtVhh3x0-JQ',
        'Content-Type': 'application/json',
    }
    url_prefix = 'http://dreamtown.synology.me:5182'
    logger.info("***Step1:Hello World")
    requests_get(url_prefix, headers)
    logger.info("\n")

    logger.info("***Step2:Download Data")
    requests_get('{}/backtest/download_data'.format(url_prefix), headers)
    logger.info("\n")

    logger.info("***Step3:Generate Signals")
    # strategy_type=cointegration&
    # backtest_start=2023-01-01&backtest_end=2023-12-31&
    # stk0=02359&stk1=603259&
    # loss_limit=-0.1&
    # lookback=40&
    # enter_threshold=2.0&exit_threshold=0.5&init_cash=100000
    signal_data = {
        "strategy_type": "cointegration",
        "backtest_start": "2023-01-01",
        "backtest_end": "2030-12-31",
        "stk0": "02359",
        "stk1": "603259",
        "loss_limit": -0.1,
        "lookback": 40,
        "enter_threshold": 2.0,
        "exit_threshold": 0.5,
        "init_cash": 100000
    }
    requests_get('{}/backtest/signals'.format(url_prefix), headers=headers, params=signal_data)
    logger.info("\n")

    logger.info("***Step4:Hello World Again")
    requests_get(url_prefix, headers)
