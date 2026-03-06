from flask import Flask #import Flask class from flask module

app = Flask(__name__) # system variable __name__ is passed to Flask constructor to determine the root path of the application

#DYNAMIC URLS/routes 
@app.route("/") # decorator that tells Flask which URL should trigger the function that follows it. In this case, it means that when the root URL ("/") is accessed, the hello_world() function will be called.
def hello_world():
    return "<h1>Hello, changeorld but biggerrrooooooooooor!</h1>"

@app.route("/bye")  # when the URL "/bye" is accessed, the bye() function will be called.
def bye():
    return "<h1>bye bro</h1>"
#debug mode is enabled to allow for automatic reloading of the application when changes are made to the code, and to provide detailed error messages in the browser if an error occurs.

@app.route("/greet/<name>") # when the URL "/greet/<name>" is accessed, the greet() function will be called, and the value of <name> will be passed as an argument to the function.
def greet(name): #important to hv name in the url and pass it to the function
    return f"<h1>Hello, {name}!</h1>" # the function returns a personalized greeting message that includes the value of <name>.


