from utils import *


if __name__ == "__main__":
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3NTM5NDE2MTIuNjE2OTg4NH0.yCFxWDdynhA2r38uHT-6reIjRS1jhDATWriyKa8Bo90',
        'Content-Type': 'application/json',
    }
    url_prefix = 'http://dreamtown.synology.me:5186'
    logger.info("***Step1:Hello World,{}".format(get_current_time()))
    requests_get(url_prefix, headers)
    logger.info("\n")

    logger.info("***Step2:Download Data")
    requests_get('{}/incremental_download_data'.format(url_prefix), headers)
    logger.info("\n")

    logger.info("***Step3:Download Data Weekend")
    requests_get('{}/incremental_download_data_weekend'.format(url_prefix), headers)
    logger.info("\n")

    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get(url_prefix, headers)
