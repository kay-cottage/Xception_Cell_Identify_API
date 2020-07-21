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

    # create model
    model = load_model(r"\result\model_fine_ep1_valloss3.745.h5")

    # load class names
    classes = []
    with open(r"\result\classes.txt", 'r') as f:
        classes = list(map(lambda x: x.strip(), f.readlines()))
        print(classes)

    # load an input image
    img = image.load_img(r"\images\2.jpg", target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
   # print(x)

    # predict
    pred = model.predict(x)[0]
    global result
    result = [(classes[i], float(pred[i]) * 100.0) for i in range(len(pred))]
    print(result)
    return json.dumps(result)
    




#设置路由
@app.route("/",methods = ["GET"])

def upload():
    main()
    return json.dumps(result)



#启动路由
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
