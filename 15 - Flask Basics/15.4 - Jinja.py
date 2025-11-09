# Building URL Dynamically
# Variable Rule


# Jinja 2 template engine :- {{ }} expressions to print output in html 
# {%...%} is used for conditional statements, loops etc..
# {#...#} is for comments

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
  return "<html><h1>Hello World!!</h1></html>"

@app.route('/contact', methods=['GET'])
def contact():
  return render_template('contact.html')

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/submit', methods=['GET','POST'])
def submit():
  if request.method == 'POST':
    name = request.form['name']
    return f'Hello {name}'
  return render_template('getresult .html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
  res = ''
  if score >=50:
    res = 'PASS'
  else:
    res = 'FAIL'
  return render_template('result.html', results=res)

@app.route('/successres/<int:score>')
def successres(score):
  res = ''
  if score >=50:
    res = 'PASS'
  else:
    res = 'FAIL'
  
  expression= {'score': score, 'res': res}
  
  return render_template('result1.html', results=expression)

@app.route('/fail/<int:score>')
def fail(score):
  return render_template('result.html', results = score)

@app.route('/getresults', methods=['GET', 'POST'])
def getresults():
  total_score = 0
  if request.method == 'POST':
    science = float(request.form['Science'])
    maths = float(request.form['maths'])
    C = float(request.form['C'])
    ml = float(request.form['ML'])
    total_score = (science + maths + C + ml)
  return redirect(url_for('successres', score=total_score))

if __name__ == "__main__":
  app.run(debug=True)
  