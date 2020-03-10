from flask import Flask, render_template, request, flash, url_for, redirect
from flask_cors import CORS, cross_origin
from db.db_functions import *
import base64
from utilities.utils import *


app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['FLASK_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.app = app
db.init_app(app)


@app.route('/')
@cross_origin()
def index():
    flash("Welcome to the Image Store ", "info")
    return render_template("main.html", upload_page=url_for('upload'))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("upload.html")

    # for post method i.e., for storing the image in database
    f = request.files['file']
    if (f.filename == '') or ("image" not in f.mimetype):
        flash("File should be an image file", "danger")
        return render_template("error.html")

    password_protected = True if 'password_protected' in request.form else False
    password = get_hash(request.form['password']) if password_protected else None

    filename = f.filename
    print(filename)
    content = request.files['file'].read()
    shortenedURL = write_to_db(filename, content, password_protected, password)
    flash("Successfully uploaded, please note the below shortened URL to access the uploaded file in future ", "info")
    return render_template("success.html", shortenedURL=makeURL(shortenedURL))


@app.route('/retrieve/<string:imageURL>', methods=['GET'])
def fetch(imageURL):
    status, image = get_from_db(imageURL)
    if status is False:
        flash("not found, try with a different URL", "danger")
        return render_template("error.html")
    print(image.passwordOpted)
    if image.passwordOpted:
        flash("Please enter your password to access the image.", "info")
        return render_template("auth-predisplay.html", imageURL=imageURL)

    return display_image(image)


def display_image(image):
    increment_visit(image)

    flash("number of times retrieved: " + str(image.visitsCount), "info")
    return render_template("display.html", content=base64.b64encode(image.content).decode())


@app.route('/retrieve/<string:imageURL>/verify_password', methods=['POST'])
def verify_password(imageURL):
    password = get_hash(request.form['password'])
    print(password)
    status, image = get_from_db(imageURL)
    if status is False:
        flash("not found, try with a different URL", "danger")
        return render_template("error.html")

    if password == image.password:
        return display_image(image)

    flash("Invalid password, please try again", "danger")
    return render_template("error.html"), 400


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=app.debug)
