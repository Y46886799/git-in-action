from utils import *


if __name__ == "__main__":
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3NTM2ODIxMzEuNDQ1NzM2Nn0.nHoiPQYeyOg5hnQ3NCgowSp5RHmBbHlSRtVhh3x0-JQ',
        'Content-Type': 'application/json',
    }
    url_prefix = 'http://dreamtown.synology.me:5182'
    logger.info("***Step1:Hello World,{}".format(get_current_time()))
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

    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get(url_prefix, headers)
