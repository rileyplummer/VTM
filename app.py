from flask import Flask
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

@app.route('/add_inputs', methods = ['POST'])
def add_inputs():
    if request.method == 'POST':
        form = request.form
        radius = form['radius']
        height = form['height']
        print(radius)
        print(height)
        calculate= radius + height
        print(calculate)
        return render_template('estimate.html', pageTitle='BPA RPA Assignment', contacts = calculate) 
    return render_template('estimate.html', pageTitle='BPA RPA Assignment', contacts = calculate) 

if __name__ == '__main__':
    app.run(debug=True)

