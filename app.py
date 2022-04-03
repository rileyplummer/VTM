from flask import Flask
from flask import request, render_template, redirect, url_for

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

@app.route('/add_inputs', methods=['GET','POST'])
def add_inputs():
    if request.method == 'POST':    
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        print(radius)
        print(height)
        calculate = (((3.14*(radius**2))+(2*3.14*radius*height))/144*25)+(((3.14*(radius**2))+(2*3.14*radius*height))/144*15)
        print(calculate)
        return render_template('estimate.html', pageTitle='Estimate', estimate =calculate) 
    return render_template('estimate.html')


if __name__ == '__main__':
    app.run(debug=True)

