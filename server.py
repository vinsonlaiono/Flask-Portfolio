from flask import Flask, render_template  

app = Flask(__name__)     


@app.route('/')                           
def hello_world():
    return render_template('myPortfolio.html')  


@app.route('/success')
def success():
    return render_template('aboutMe.html')

@app.route('/webPage')
def webPage():
    return render_template('webPage.html')



if __name__=="__main__":
    app.run(debug = True)   