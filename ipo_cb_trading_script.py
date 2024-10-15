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

    logger.info("***Step2:Download convertible bond IPO Data")
    try:
        requests_get('{}/current_cb_ipo'.format(base_url), headers)
    except Exception as e:  
        logger.error(f"Download convertible bond IPO Data Error: {e}")
    logger.info("\n")

    logger.info("***Step3:Participate convertible bond IPO")
    try:
        requests_get('{}/auto_bond_conv'.format(base_url), headers)
    except Exception as e:
        logger.error(f"Participate convertible bond IPO Error: {e}")
    logger.info("\n")

    logger.info("***Step4:Hello World Again,{}".format(get_current_time()))
    requests_get(base_url, headers)
