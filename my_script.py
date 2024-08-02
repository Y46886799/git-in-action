import requests  

def requests_get(url:str)
	# 发送 GET 请求  
	response = requests.get(url)  

	# 检查响应状态  
	if response.status_code == 200:  
	    print("请求成功!")  
	    # 输出响应内容  
	    print(response.json())  # 将响应内容解析为 JSON  
	else:  
	    print("请求失败:", response.status_code)


def requests_post(url:str, data)
	# 发送 POST 请求  
	response = requests.post(url, json=data)  

	# 检查响应状态  
	if response.status_code == 200:  
	    print("数据已创建!")  
	    print(response.json())  
	else:  
	    print("请求失败:", response.status_code)



if __name__ == "__main__":
	data = {
			  "start_date": "2023-08-21",
			  "end_date": "2030-12-31",
			  "backtest_config": "grid_arrj_1d",
			  "strategy_name": "trend_following",
			  "grid_low": 6.25,
			  "grid_high": 10.35,
			  "grid_num": 6
			}
	requests_post('http://dreamtown.synology.me:5181/grid/signals', data)