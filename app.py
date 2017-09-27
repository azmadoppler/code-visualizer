from flask import Flask, render_template , request
from flask_bootstrap import Bootstrap
import os;
import subprocess;

app = Flask(__name__)

# Make sure to install 'Flask-Bootstrap'
Bootstrap(app)


@app.route('/')
def index():
    with open('all_command.txt' , 'r') as f:
        content = [line.strip() for line in f]
    name = []
    command = []

    for item in content:
        spliter = item.split(',')
        name.append(spliter[0])
        command.append(spliter[1])
    output_value = zip(name,command)
    return render_template('index.html',output_value=output_value)

@app.route('/execute')
def execute():
    command = request.args.get('command')
    execute_command = command.split( )
    execution = subprocess.check_output(execute_command, shell=True)
    # return render_template('result.html',command=command,execution=execution)
    return render_template('result.html', command = command , execution = execution)



if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)
