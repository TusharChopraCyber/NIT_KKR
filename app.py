# app.py

from flask import Flask, render_template, request
from crypto import main  # Import the main function from crypto.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tx_hash = request.form.get('tx_hash')
        result = main(tx_hash)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
