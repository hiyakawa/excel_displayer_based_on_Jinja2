from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello', methods = ['POST'])

def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()