import requests
import json
import base64
# from PIL import Image


def encode_image(image_path):       # 编码本地图片的函数
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# 1.url
model_url = 'http://10.7.20.87:8000/v1/chat/completions'


# 2.data
image_path = "jieti.jpg"
# image_path = 'vbench.jpg'
base64_image = encode_image(image_path)     # 编码本地图片
data = {"model": "Qwen2-VL-7B",
        "messages": [{"role": "system",
                      "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
                     {"role": "user",
                      "content": [
                          {"type": "image_url",
                           "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                          {"type": "text",
                           "text": "请解答图中的题"}]}],
        "temperature": 0.7,
        "top_p": 0.8,
        "repetition_penalty": 1.05,
        "max_tokens": 1024}


# 3.将字典转换为 JSON 字符串
json_payload = json.dumps(data)


# 4.发送 POST 请求
headers = {'Content-Type': 'application/json'}
response = requests.post(model_url, data=json_payload, headers=headers)


# 5.打印响应内容
print(response.json().get("choices", [])[0].get("message", []).get("content", []))      # 命令行启动，用这个打印
# print(response.json())



