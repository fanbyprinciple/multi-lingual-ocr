# To be expanded to cover the OCR
from flask import Flask, render_template,request
from ocr_from_image_module import *
from urllib.parse import unquote

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/recog', methods=['POST'])
def recog():

    data = request.get_data().decode("utf-8")
    print("I got this from html")
    d = unquote(data.split('=')[1])
    print(unquote(data.split('=')[1]))
    result = recog_image(d)
    print('result for flask: ', result)
    # result = 'dummy results'
    return {'data': result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)


