from flask import Flask, render_template

app = Flask(__name__)

@app.route('/loading')
def loading_page():
    return render_template('index.html')  # This is your loading page (index.html)

@app.route('/')
def homepage():
    return "Welcome to the homepage!"  # This is the homepage, you can use a template here as well.

if __name__ == '__main__':
    app.run(debug=True)
