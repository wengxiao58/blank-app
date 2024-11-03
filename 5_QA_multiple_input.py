import requests
import json
import base64


def encode_image(image_path):       # 编码本地图片的函数
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# 1.url
model_url = 'http://10.7.20.87:8000/v1/chat/completions'

# 2.data
data = {"model": "Qwen2-VL-7B",     # 初始化data
        "messages": [{"role": "system",
                      "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},],
        "temperature": 0.7,
        "top_p": 0.8,
        "repetition_penalty": 1.05,
        "max_tokens": 1024}


# 纯语言的多轮对话
# text_ls = ["什么是大语言模型", "都有哪些", "写一首诗赞美一下他们"]

# 循环text_ls里面的所有问题
# for num in range(5):
while 1:
    text = input('Q:')
    if text == 'end':
        break

    m = {"role": "user", "content":[]}
    if '<img>' in text:
        text, query_image_url = text.split('<img>')
        # m =b
        m['content'].append({"type": "image_url",
                            "image_url": {"url": query_image_url}})
    m['content'].append({"type": "text",
                        "text": text})
    data["messages"].append(m)   # 将用户问题输入大模型的prompt

    # 3.将字典转换为 JSON 字符串
    json_payload = json.dumps(data)

    # 4.发送 POST 请求
    headers = {'Content-Type': 'application/json'}
    response = requests.post(model_url, data=json_payload, headers=headers)

    data["messages"].append({"role": "assistant",   # 将大模型的输出加入到data(prompt)，用于下一次输入
                            "content": [
                                {"type": "text",
                                 "text": response.json().get("choices", [])[0].get("message", []).get("content", [])}, ], })

    print("User: ", text)
    print("Answer: ", response.json().get("choices", [])[0].get("message", []).get("content", []))
    print("-"*50)

# print(response.json())


