import requests
import json
import base64


# 1.url
model_url = 'http://10.7.20.87:8000/v1/chat/completions'


# 2.data
# query_image_url = "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
query_image_url = "https://cdn.outsideonline.com/wp-content/uploads/2023/03/Funny_Dog_H.jpg?crop=16:9&width=960&enable=upscale&quality=100"

# query_image_url = input('输入图片链接：')

data = {"model": "Qwen2-VL-7B",
        "messages": [{"role": "system",
                      "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
                     {"role": "user",
                      "content": [
                          {"type": "image_url",
                           "image_url": {"url": query_image_url}},
                          {"type": "text",
                           "text": "Describe this image."}]}],
                           # "text": "Describe this image."}]}],
        "temperature": 0.7,
        "top_p": 0.8,
        "repetition_penalty": 1.05,
        "max_tokens": 512}


# 3.将字典转换为 JSON 字符串
json_payload = json.dumps(data)


# 4.发送 POST 请求
headers = {'Content-Type': 'application/json'}
response = requests.post(model_url, data=json_payload, headers=headers)

# 5.打印响应内容
print(response.json().get("choices", [])[0].get("message", []).get("content", []))      # 命令行启动，用这个打印
# print(response.json())



