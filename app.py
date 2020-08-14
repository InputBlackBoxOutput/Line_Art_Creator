# Line Art Creator: Convert images to line art using openCV
#
# @file  : app.py
# @brief : Provides entry-point and framework 
# @author: Rutuparn Pawar <InputBlackBoxOutput>
# @date_created : 14 Aug 2020

import edges
import thinner
#--------------------------------------------------------------------------------------
from PIL import Image
import numpy as np
from io import BytesIO
from base64 import b64encode

#------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request
app = Flask(__name__)
app.config['SECRET_KEY'] = '4d12bc03d6bdfc7a945a65d1316490fa'

#------------------------------------------------------------------------------------------------
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

#------------------------------------------------------------------------------------------------
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

class UploadForm(FlaskForm):
    photo = FileField(' ', validators=[FileAllowed(['jpg', 'png', 'jpeg'], u'Image only!'), FileRequired(u'An image is required!')])
    submit = SubmitField(u'Convert to line art')

#------------------------------------------------------------------------------------------------
@app.route('/', methods=['GET','POST'])
def run():
    form = UploadForm()

    if form.validate_on_submit():
        print(form.photo.data)

        # It works do not touch it :-)
        image_stream = form.photo.data.stream
        img = Image.open(image_stream)
        pil_image = img.convert('RGB') 

        cv_image = np.array(pil_image) 
        cv_image =cv_image[:, :, ::-1].copy() 

        img = 255 - edges.detectEdges(cv_image, isFile=False)
        # img = thinner.thinEdges(img)

        pil_img = Image.fromarray(img)
        byteIO = BytesIO()
        pil_img.save(byteIO, "PNG")
        byteArr = byteIO.getvalue()
        encoded = b64encode(byteArr)

        result = "True"
    else:
        img = np.zeros((100,100))
        pil_img = Image.fromarray(img)
        pil_img = pil_img.convert('RGB')
        
        byteIO = BytesIO()
        pil_img.save(byteIO, "PNG")
        byteArr = byteIO.getvalue()
        encoded = b64encode(byteArr)
        result = "False"

    return render_template('index.html', result=result, form=form, encoded_photo=encoded.decode('ascii'))

#------------------------------------------------------------------------------------------------
# Time to have fun!
@app.route('/fun')
def fun():
    return redirect("https://inputblackboxoutput.github.io/Tic-Tac-Toe-Online/") 

#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)  

#------------------------------------------------------------------------------------------------
# EOF