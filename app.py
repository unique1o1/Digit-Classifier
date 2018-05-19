from flask import Flask, render_template, request
import re
import base64
import io
import numpy as np
from PIL import Image
from classifier import model as ml
model, graph = ml()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def convertImage(imgData1):
    img = Image.open(io.BytesIO(
        base64.b64decode(re.search(r'base64,(.*)', str(imgData1)).group(1))))

    return img


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        imgData = request.get_data()
        img = convertImage(imgData).convert('L')
        img = img.resize((28, 28))
        img = np.asarray(img).astype('float32')/255
        img.resize(1, 28, 28, 1)
        with graph.as_default():
            return str(model.predict(img).argmax())


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
