# 编写人: Bonnie
# 开发时间：2024/2/25 19:34

from flask import Flask, request, send_file, make_response,Response
from flask_cors import CORS
import json
import random

app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://yiyan.baidu.com"}})

data={}
url="http://127.0.0.1:3000"


def make_json_response(data, status_code=200):

    response = make_response(json.dumps(data), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/upload_image_url",methods=['POST'])
async def upload_image_url():
    """
      上传照片
    """
    imageUrl=request.json.get('imageUrl','')
    data["imgurl"]=imageUrl
    return make_json_response({"message":"图片上传成功"})


@app.route("/upload_prompt",methods=['POST'])
async def upload_prompt():
    prompt=request.json.get("prompt","")
    data["prompt"]=prompt

    response=post_to_model()

    if(response==flase):
         return make_json_response({"message": "结果返回失败"})
    else:
        return make_json_response({"message": "结果返回成功，请点击链接查看："+response.imageUrl})
        # return send_file('logo.png', mimetype='image/png')


def post_to_model():
    json_data = json.dumps(data)
    url="http://backend-url.com/api"
    headers={'Content-Type':'application/json'}
    #发送请求
    response = requests.post(url, data=json_data, headers=headers)
    if response.status_code == 200:
        print('Success:', response.json())
        return response.content
    else:
        print('Error:', response.status_code, response.text)
        return false


@app.route("/logo.png")
async def plugin_logo():
    return send_file('logo.png', mimetype='image/png')

def generate_response():
    """
    生成回答
    """
    prompt = "上传图片链接和提示信息来得到返回的结果"
    return make_json_response({ "prompt": prompt})

@app.route("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.host_url
    with open(".well-known/ai-plugin.json", encoding="utf-8") as f:
        text = f.read().replace("PLUGIN_HOST", host)
        return text, 200, {"Content-Type": "application/json"}


@app.route("/.well-known/openapi.yaml")
async def openapi_spec():
    with open(".well-known/openapi.yaml", encoding="utf-8") as f:
        text = f.read()
        return text, 200, {"Content-Type": "text/yaml"}


@app.route('/')
def index():
    return 'welcome to my webpage!'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



