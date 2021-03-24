# To be expanded to cover the OCR
from flask import Flask, render_template,request
from ocr_from_image import *

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/recog', methods=['POST'])
def recog():

    data = request.get_data().decode("utf-8")
    data = data.replace("%2F", "/")
    data = data.replace("+", " ")
    result = recog_image(data.split('=')[1])
    print('result for flask: ', result)
    # result = 'dummy results'
    return {'data': result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)


