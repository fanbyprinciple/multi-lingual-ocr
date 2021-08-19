# General Readme

1. install pytessearct, tesseract-ocr
2. cv2
3. transformers
4. unidecode
5. googletrans=4.0
6. flask
7. sentencepiece
8. tesseract-ocr-ben
offline using marianmt: 

![](offline_works.png)

Marianmt not available.

# OCR application

`HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python3 ocr_from_image_marianmt.py`

## Installation in linux

Important link:
`https://linuxhint.com/install-tesseract-ocr-linux/`

1. Installing pip requirements
`pip3 install -r requirements.txt`

2. Installing in linux
`sudo apt-get install tesseract-ocr`

3. For installing all language pack use
`apt-get install tesseract-ocr-all`

4. For bengali use:
`apt-get install tesseract-ocr-ben`

Or download language pack manually from github.

## Initially using tesseract.

![](./img/Screen.png)

## Other Tools to leverage for ocr

1. OCRopus - https://github.com/ocropus/ocropy

2. Ocular - https://github.com/tberg12/ocular

3. https://medium.com/better-programming/beginners-guide-to-tesseract-ocr-using-python-10ecbb426c3d

## google translate

It is working well with python

![](./img/googletrans.png)

## Tesseract 4.1

From : `https://nanonets.com/blog/ocr-with-tesseract/`

![](./img/tesseract_cots.png)

Tesseract 4.00 includes a new neural network subsystem configured as a text line recognizer.
It has its origins in OCRopus' Python-based LSTM implementation but has been redesigned for Tesseract in C++.
The neural network system in Tesseract pre-dates TensorFlow but is compatible with it, as there is a network description language called Variable Graph Specification Language (VGSL), that is also available for TensorFlow.
To recognize an image containing a single character, we typically use a Convolutional Neural Network (CNN). 
Text of arbitrary length is a sequence of characters, and such problems are solved using RNNs and LSTM is a popular form of RNN. 
Read this post to learn more about LSTM.

![](./img/t5_preprocessed.png)

LSTMs are great at learning sequences but slow down a lot when the number of states is too large. 
There are empirical results that suggest it is better to ask an LSTM to learn a long sequence than a short sequence of many classes.
Tesseract developed from OCRopus model in Python which was a fork of a LSMT in C++, called CLSTM. 
CLSTM is an implementation of the LSTM recurrent neural network model in C++, using the Eigen library for numerical computations.

The only language pack installed in macOS Tesseract is English, which is contained in the eng.traineddata file.

![](./img/sub_optimal.png)

So what are these Tesseract files?

`eng.traineddata` is the language pack for English.
`osd.traineddata` is a special data file related to orientation and scripts.
`snum.traineddata` is an internal serial number used by Tesseract.
pdf.ttf is a True Type Format Font file to support pdf renderings.

Got bengali text:
![](./img/bengali_text.png)

## Checklist:

1. make pytesseract work - done

tesseract documentation:

`https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc`

tessseract sorted!

1. bengali translation - done

![](./img/bengali_translated.png)

1. get boxes around text - not done

`https://www.pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/`


## To run

1. put the pdf you want to extract in the pdf folder

2. run pdf_to_img first tp convert pdf to img

`python3 pdf_to_img.py`

3. run ocr_from_multiple_img for convertig img to script

`python3 ocr_from_multiple_img.py`

4. for using the flask server

`python3 app.py`

![](./img/flaskpng)

## Things to do 

1. improve UI
2. Add language detection feature
3. Add possibility to directly convert from pdf
4. integrate docx documents

## for offline installation

Checkout the offline folder

# using MarianMT

1. `pip3 install transformers`
2. `pip3 install sentencepiece`
3. `pip3 install mosestokenizer`
4. You also need to install pytorch in the base

