from flask import Flask, render_template, request
from config import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    token1 = request.form['token1']
    token2 = request.form['token2']    
    model = TokenSimilarity()
    model.load_pretrained('indobenchmark/indobert-base-p2')
    a = model.predict(token1, token2)
    return render_template('pass.html', a=a, t1=token1, t2=token2)

if __name__ == '__main__':
    app.run(debug=True)