# coding:utf-8
import time
import matplotlib.image as processimage
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from flask import Flask
import os
import json
from flask import request
import argparse
import numpy as np
from keras.applications.xception import preprocess_input
from keras.preprocessing import image
from keras.models import load_model



app = Flask(__name__)
app.config['DEBUG'] = True






def main():

    # create model,加载细胞形态学识别模型model_identify_cell.h5文件
    model = load_model("model_identify_cell.h5")

    # load class names
    classes = []
    with open("classes.txt", 'r') as f:
        classes = list(map(lambda x: x.strip(), f.readlines()))
        print(classes)

    # load an input image
    img = image.load_img("2.jpg", target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
   # print(x)




    # 预测打印出识别结果
    pred = model.predict(x)[0]
    global result
    result = [(classes[i], float(pred[i]) * 100.0) for i in range(len(pred))]
    print(result)
    
    #返回json格式识别结果
    return json.dumps(result)
    




#设置路由，POST方法请求
@app.route("/",methods = ["POST"])
def upload():
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "上传失败"
    file_obj.save("2.jpg")
    print("上传成功")
    main()
    os.remove("2.jpg")
    return json.dumps(result)



#启动路由
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
