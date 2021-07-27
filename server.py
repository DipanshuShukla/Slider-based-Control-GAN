from flask import Flask, render_template, url_for, request, redirect, session, flash
#from werkzeug.utils import secure_filename
#from tempfile import mkdtemp
#from flask_session import Session
import PIL.Image
import numpy as np



app = Flask("__name__")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
	return "Home Page"

if __name__ == '__main__':
    app.run()