from flask import Flask,render_template
import os


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/testpage')
def testpage():
   imgURL = 'static/test.png'
   os.system(r"python caculate.py")
   return render_template('testpage.html',imgURL=imgURL)




if __name__ == '__main__':
   app.run()


   