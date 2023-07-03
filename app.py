from flask import Flask,render_template,request,jsonify,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('inner-page.html')



@app.route('/nlpprojects')
def nlpprojects():
    return render_template('nlpproject.html')

@app.route('/mlprojects')
def mlprojects():
    return render_template('mlproject.html')

@app.route('/cvprojects')
def cvprojects():
    return render_template('cvproject.html')


if __name__=="__main__":
    app.run(debug=True)

