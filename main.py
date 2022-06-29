from flask import Flask, request, render_template, url_for,redirect

app = Flask(__name__, template_folder='templates')


@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True , host= '0.0.0.0')
        