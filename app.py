from flask import Flask

app = Flask(__name__)
app.secret_key = "secrete key"
#path = os.getcwd()
#UPLOAD_FOLDER =  path + '\\upload'
UPLOAD_FOLDER = 'C:\\Users\\Nobby.Munguza\\PycharmProjects\\upload-app\\upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
