from utils import *

if __name__ == "__main__":
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDY4ODY3OTlAMTYzLmNvbSIsImV4cGlyZXMiOjE3NTk5MTU5NzguNjU5MjV9.Id-bCCsi22NsmnhvYEhE5U0QWd91FFXBzspi18l_RUU',
        'Content-Type': 'application/json',
    }
    base_url = "http://dreamtown.synology.me:8000"
    logger.info("***Step1:Hello World,{}".format(get_current_time()))
    requests_get(base_url, headers)
    logger.info("\n")

    logger.info("***Step2:The first account start to reverse repo.")
    try:
        params = {
                  "account_num": 1,
                  "market_type": "sh",
                  "days": "1days"
        }
        requests_post('{}/reverse_repo'.format(base_url),headers, params)
    except Exception as e:
        logger.error(f"The third account start to reverse repo Error: {e}") 
    logger.info("\n")

    logger.info("***Step2:The seconde account start to reverse repo.")
    try:
        params = {
                  "account_num": 2,
                  "market_type": "sh",
                  "days": "1days"
        }
        requests_post('{}/reverse_repo'.format(base_url),headers, params)
    except Exception as e:
        logger.error(f"The third account start to reverse repo Error: {e}") 
    logger.info("\n")

    logger.info("***Step2:The third account start to reverse repo.")
    try:
        params = {
                  "account_num": 3,
                  "market_type": "sh",
                  "days": "1days"
        }
        requests_post('{}/reverse_repo'.format(base_url),headers, params)
    except Exception as e:
        logger.error(f"The third account start to reverse repo Error: {e}") 
    logger.info("\n")

    logger.info("***Step2:The forth account start to reverse repo.")
    try:
        params = {
                  "account_num": 4,
                  "market_type": "sh",
                  "days": "1days"
        }
        requests_post('{}/reverse_repo'.format(base_url),headers, params)
    except Exception as e:
        logger.error(f"The third account start to reverse repo Error: {e}") 
    logger.info("\n")

    logger.info("***Step2:The fifth account start to reverse repo.")
    try:
        params = {
                  "account_num": 5,
                  "market_type": "sh",
                  "days": "1days"
        }
        requests_post('{}/reverse_repo'.format(base_url),headers, params)
    except Exception as e:
        logger.error(f"The third account start to reverse repo Error: {e}") 
    logger.info("\n")

    logger.info("***Step3:Hello World Again,{}".format(get_current_time()))
    requests_get(base_url, headers)

    import time
    # 暂停 60 秒  
    time.sleep(60) 
