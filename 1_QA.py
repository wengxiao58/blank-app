import requests
import json

# 1.url
model_url = 'http://10.7.20.87:8000/v1/chat/completions'

text = input('请输入问题：')

# 2.data，字典类型（Key-Value）
data = {"model": "Qwen2-VL-7B",
        "messages": [{"role": "system",  # 下面的content是 系统命令，一般不要改
                      "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
                     {"role": "user",    # 下面的content是 用户命令，一般改这里
                      "content": text}],
        "temperature": 0.7,
        "top_p": 0.8,
        "repetition_penalty": 1.05,
        "max_tokens": 1024}


# 3.将字典转换为 JSON 字符串
json_payload = json.dumps(data)

# 4.发送 POST 请求
# requests.post可将数据data发送到服务器时使用
headers = {'Content-Type': 'application/json'}
response = requests.post(model_url, data=json_payload, headers=headers)


# 5.打印响应内容
# 命令行启动，用这个打印
print(response.json().get("choices")[0].get("message").get("content"))
# print(response.json().get("choices", [])[0].get("message", []).get("content", []))
# print(response.json())



