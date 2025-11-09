from flask import Flask

app = Flask(__name__) # Creates an instance of the flask class, which will be your WSGI(Web Server Gateway Interface) application

@app.route("/")
def welcome():
  return 'Hello World.!.!.'

@app.route('/contact')
def contact():
  return 'Welcome to the contact page'
# Entry point of any application in .py file
if __name__ == "__main__":
  app.run(debug=True) 
  # app.run()
  # debug = True automatically restarts the server and updates the changes