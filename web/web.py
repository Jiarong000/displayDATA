from flask import Flask,render_template
import os


app = Flask(__name__)

@app.route('/')
def page():
   imgURL = 'static/test.png'
   os.system(r"python caculate.py")
   return render_template('testpage.html',imgURL=imgURL)




if __name__ == '__main__':
   app.run()


   