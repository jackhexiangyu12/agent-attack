from time import strftime

import requests
import json
import datetime

# 定义API的基础URL和密钥
api_url = 'https://rg-jdroboark.azure-api.net/openai/deployments/gpt-4-turbo/chat/completions?api-version=2023-12-01-preview'
headers = {
    'api-key': 'dbcb628573214e3997fa7c513e63f239',
    'Content-Type': 'application/json'
}

# 读取输入文件
input_file_path = 'input6_1.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    input_lines = file.read()

# 解析输入数据
# prompt_line = input_lines[0].strip()  # 由于prompt后面紧跟着冒号，所以直接使用strip()去除空白字符
# example = input_lines[1].strip()
# question = input_lines[2].strip()
# schema_type = input_lines[3].strip()
# schema = input_lines[4].strip()  # 注意这里多了一个额外的空格，需要使用lstrip()去除

# 构建请求的数据
data = {
    "messages": [
        {
            "role": "user",
            "content": "你是谁"
        }
    ]
}
#
# 计算时长post请求到API
start_time = datetime.datetime.now()

# 发送POST请求到API
response = requests.post(api_url, json=data, headers=headers)

# 计算时长
end_time = datetime.datetime.now()
duration = end_time - start_time
print(f"Duration: {duration}")


# 检查响应状态码是否成功
if response.status_code == 200:
    # 解析响应数据
    response_data = response.json()
    output_text = response_data['choices'][0]['message']['content']

    # 保存到输出文件
    output_file_path = input_file_path + f'_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        # 保存duration
        file.write(f"Duration: {duration}\n\n")
        file.write(output_text)
    print(f"Output saved to {output_file_path}")
else:
    print(f"Error: Unable to retrieve data from API, status code: {response.status_code}")