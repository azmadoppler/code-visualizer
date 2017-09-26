from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os;
import subprocess;

app = Flask(__name__)

# Make sure to install 'Flask-Bootstrap'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/script')
def script():
    # os.system("dir")
    test_ls = subprocess.check_output(['ls'])
    return test_ls

@app.route('/script2')
def script2():
    os.system("mkdir test2")
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
