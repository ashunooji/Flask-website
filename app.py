from flask import Flask, render_template,request,flash,redirect,url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

model = load_model('models/apple2.h5')

categories=['The apple leaf is healthy','This apple leaf has multiple diseases','This apple leaf has rust disease: Apply SERENADE fungicide to prevent disease','This apple leaf has scab: Apply liquid copper soap on the leaf']


def model_predict(img_path,model):
    test_image=image.load_img(img_path,target_size=(224,224))
    test_image=image.img_to_array(test_image)
    test_image=test_image/255
    test_image=np.expand_dims(test_image,axis=0)
    result=model.predict(test_image)
    return result


@app.route('/',methods=['POST','GET'])
def recv():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            image.save('static/uploads/'+image.filename)
            image_filename = 'uploads/'+image.filename
            file_path = 'static/uploads/'+image.filename
            result = model_predict(file_path,model)
            pred_class=result.argmax()
            output=categories[pred_class]
            return render_template('index.html',image_filename=image_filename,out=output)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0')